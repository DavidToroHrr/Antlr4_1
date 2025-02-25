import sys
from antlr4 import *
from FormulaLexer import FormulaLexer
from FormulaParser import FormulaParser
from FormulaVisitor import FormulaVisitor
import pandas as pd
import matplotlib.pyplot as plt

class MyVisitor(FormulaVisitor):
    def __init__(self, data):
        self.data = data  # DataFrame con los datos cargados
        self.results = {}  # Almacenar resultados de múltiples fórmulas

    def visitFile(self, ctx):
        for formula in ctx.formula():
            result = self.visit(formula)
            if result is not None:
                self.results[formula.getText()] = result  # Guardamos el resultado
        return self.results

    def visitFormula(self, ctx):
        return self.visit(ctx.expression())

    def visitNumber(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == FormulaParser.MUL:
            return left * right
        elif ctx.op.type == FormulaParser.DIV:
            return left / right
        elif ctx.op.type == FormulaParser.MOD:
            return left % right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == FormulaParser.ADD:
            return left + right
        else:
            return left - right

    def visitFunctionCall(self, ctx):
        func_name = ctx.ID().getText()
        args = [self.visit(arg) for arg in ctx.expression()]
        print(f"Función: {func_name}, Argumentos: {args}")  # Depuración

        # Convertir nombres de columna en sus valores
        for i in range(len(args)):
            if isinstance(args[i], str) and args[i] in self.data.columns:
                args[i] = self.data[args[i]]

        if not args or any(arg is None for arg in args):
            raise ValueError(f"Los argumentos para la función '{func_name}' no son válidos: {args}")

        resultado = None

        if func_name == 'suma':
            resultado = args[0].sum()
        elif func_name == 'promedio':
            resultado = args[0].mean()
        elif func_name == 'mediaPonderada':
            resultado = (args[0] * args[1]).sum() / args[1].sum()
        elif func_name == 'desviacion':
            resultado = args[0].std()
        else:
            raise ValueError(f"Función no soportada: {func_name}")

        print(f"Resultado de la función '{func_name}': {resultado}")
        return float(resultado) if resultado is not None else None

    def visitColumnReference(self, ctx):
        column_name = ctx.ID().getText()
        if column_name in self.data.columns:
            return self.data[column_name]
        else:
            raise ValueError(f"La columna '{column_name}' no existe en los datos")

def load_excel(file_path):
    try:
        return pd.read_excel(file_path, engine='openpyxl')
    except Exception as e:
        print(f"Error al cargar el archivo Excel: {e}")
        return None

def process_formulas_with_antlr(file_path, visitor):
    """
    Usa ANTLR para leer y procesar las fórmulas desde un archivo.
    """
    try:
        with open(file_path, 'r') as file:
            input_stream = InputStream(file.read())

        lexer = FormulaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FormulaParser(stream)
        tree = parser.file()  # Procesamos múltiples fórmulas
        return visitor.visit(tree)

    except Exception as e:
        print(f"Error al procesar las fórmulas: {e}")
        return {}

def plot_results(results):
    """
    Muestra los resultados en un gráfico de barras.
    """
    if not results:
        print("No hay resultados para graficar.")
        return

    formulas = list(results.keys())
    values = list(results.values())

    plt.figure(figsize=(8, 5))
    plt.barh(formulas, values, color='skyblue')
    plt.xlabel("Valor Calculado")
    plt.ylabel("Fórmulas")
    plt.title("Resultados de las Fórmulas")
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    for index, value in enumerate(values):
        plt.text(value, index, f"{value:.2f}", va='center')

    plt.show()

def export_results(results, output_format):
    df = pd.DataFrame(list(results.items()), columns=['Fórmula', 'Resultado'])

    if output_format == 'csv':
        df.to_csv('resultados.csv', index=False)
        print("Resultados exportados a 'resultados.csv'.")
    elif output_format == 'excel':
        df.to_excel('resultados.xlsx', index=False)
        print("Resultados exportados a 'resultados.xlsx'.")
    else:
        print("Formato de exportación no soportado.")

def main():
    file_path = input("Ingrese la ruta del archivo Excel: ")
    if not file_path.endswith('.xlsx'):
        print("Formato de archivo no soportado.")
        return

    df = load_excel(file_path)
    if df is None:
        return

    print("Vista previa de los datos:")
    print(df.head())

    columns = input("Ingrese las columnas a utilizar (separadas por comas): ").split(',')
    invalid_columns = [col for col in columns if col not in df.columns]
    if invalid_columns:
        print(f"Las siguientes columnas no existen: {invalid_columns}")
        return
    selected_data = df[columns]

    formulas_file = input("Ingrese la ruta del archivo de fórmulas (txt): ")
    visitor = MyVisitor(selected_data)
    results = process_formulas_with_antlr(formulas_file, visitor)

    if results:
        print("\nResultados obtenidos:")
        for formula, result in results.items():
            print(f"{formula} = {result}")

        plot_results(results)

        output_format = input("\n¿Desea exportar los resultados? (csv/excel/none): ").lower()
        if output_format in ['csv', 'excel']:
            export_results(results, output_format)

if __name__ == '__main__':
    main()
