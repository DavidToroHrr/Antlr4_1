import sys
from antlr4 import *
from FormulaLexer import FormulaLexer
from FormulaParser import FormulaParser
from FormulaVisitor import FormulaVisitor
import pandas as pd
import math

class MyVisitor(FormulaVisitor):
    def __init__(self, data):
        self.data = data  # DataFrame con los datos cargados

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
        if func_name == 'suma':
            return self.data[args[0]].sum()
        elif func_name == 'promedio':
            return self.data[args[0]].mean()
        elif func_name == 'mediaPonderada':
            return (self.data[args[0]] * self.data[args[1]]).sum() / self.data[args[1]].sum()
        elif func_name == 'desviacion':
            return self.data[args[0]].std()
        else:
            raise ValueError(f"Función no soportada: {func_name}")

def load_csv(file_path):
    """
    Carga un archivo CSV y devuelve un DataFrame de pandas.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return None

def load_excel(file_path, sheet_name=0):
    """
    Carga un archivo Excel y devuelve un DataFrame de pandas.
    """
    try:
        return pd.read_excel(file_path, sheet_name=sheet_name,engine='openpyxl')
    except Exception as e:
        print(f"Error al cargar el archivo Excel: {e}")
        return None

def preview_data(df, num_rows=5):
    """
    Muestra una vista previa de los datos (primeras filas).
    """
    if df is not None:
        print(df.head(num_rows))
    else:
        print("No hay datos para mostrar.")

def export_results(result, output_format):
    """
    Exporta los resultados a un archivo CSV o Excel.
    """
    if output_format == 'csv':
        result.to_csv('resultados.csv', index=False)
        print("Resultados exportados a 'resultados.csv'.")
    elif output_format == 'excel':
        result.to_excel('resultados.xlsx', index=False)
        print("Resultados exportados a 'resultados.xlsx'.")
    else:
        print("Formato de exportación no soportado.")

def main():
    # Carga de archivos (Fase 2)
    file_path = input("Ingrese la ruta del archivo (CSV o Excel): ")
    if file_path.endswith('.csv'):
        df = load_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = load_excel(file_path)
    else:
        print("Formato de archivo no soportado.")
        return

    preview_data(df)

    columns = input("Ingrese las columnas a utilizar (separadas por comas): ").split(',')
    invalid_columns = [col for col in columns if col not in df.columns]
    if invalid_columns:
        print(f"Las siguientes columnas no existen: {invalid_columns}")
        return
    selected_data = df[columns]

    # Solicita una fórmula al usuario
    formula = input("Ingrese una fórmula: ")
    input_stream = InputStream(formula)
    lexer = FormulaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FormulaParser(stream)
    tree = parser.formula()

    # Evalúa la fórmula usando el Visitor
    visitor = MyVisitor(selected_data)
    result = visitor.visit(tree)
    print(f"Resultado: {result}")

    # Exportar resultados (Fase 4)
    output_format = input("¿Desea exportar los resultados? (csv/excel/none): ").lower()
    if output_format in ['csv', 'excel']:
        export_results(pd.DataFrame({'Resultado': [result]}), output_format)

if __name__ == '__main__':
    main()