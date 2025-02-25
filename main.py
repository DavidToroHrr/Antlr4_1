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
        print("🔄 Procesando archivo con múltiples fórmulas...")  # 🚀 Depuración

        if not ctx.formula():
            print("❌ No se encontraron fórmulas en el árbol sintáctico.")
            return {}

        for formula in ctx.formula():
            formula_text = formula.getText()
            print(f"📌 Procesando fórmula: {formula_text}")  # 🚀 Depuración

            result = self.visit(formula)  # 👈 Aquí llamamos a `visitFormula`
            if result is not None:
                self.results[formula_text] = result
                print(f"✅ Resultado para {formula_text}: {result}")  # 🚀 Ver resultado
            else:
                print(f"⚠️ La fórmula {formula_text} devolvió None.")  # 🚀 Más depuración

        print(f"✅ Resultados finales en visitFile: {self.results}")
        return self.results

    def visitFormula(self, ctx):
        print(f"🔍 Evaluando expresión en visitFormula: {ctx.getText()}")
        result = self.visit(ctx.expression())  # Evaluamos la expresión principal

        # 🔥 Nueva validación para evitar propagación de None
        if result is None:
            print(f"❌ Error: La expresión '{ctx.getText()}' devolvió None.")
            return None

        print(f"🔹 Resultado de la fórmula: {result}")  # 🚀 Depuración
        return float(result)  # Asegurar que devuelve un número

    def visitNumber(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitMulDivMod(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()

        print(f"🛠️ Evaluando: {left} {operator} {right}")  # Depuración

        if left is None:
            print(f"❌ Error: La parte izquierda de la operación es None ({operator} {right})")
            return None
        if right is None:
            print(f"❌ Error: La parte derecha de la operación es None ({left} {operator})")
            return None

        try:
            resultado = None
            if operator == '*':
                resultado = left * right
            elif operator == '/':
                if right == 0:
                    print("❌ Error: División por cero.")
                    return None
                resultado = left / right
            elif operator == '%':
                resultado = left % right
            else:
                print(f"❌ Operador desconocido: {operator}")
                return None

            print(f"✅ Resultado de {left} {operator} {right} = {resultado}")  # Confirmar resultado
            return float(resultado)  # Asegurar retorno válido

        except Exception as e:
            print(f"❌ Error durante la operación {left} {operator} {right}: {e}")
            return None

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expression(0))  # Evalúa la primera expresión
        right = self.visit(ctx.expression(1))  # Evalúa la segunda expresión

        operator = ctx.getChild(1).getText()  # Obtener el operador

        print(f"🛠️ Evaluando: {left} {operator} {right}")  # 🔍 Depuración

        if left is None:
            print(f"❌ Error: La parte izquierda de la operación es None ({operator} {right})")
            return None
        if right is None:
            print(f"❌ Error: La parte derecha de la operación es None ({left} {operator})")
            return None

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        else:
            print(f"❌ Operador desconocido: {operator}")
            return None


    def visitFunctionCall(self, ctx):
        func_name = ctx.FUNC().getText()  # ✅ Ahora FUNC en lugar de ID
        args = [self.visit(arg) for arg in ctx.expression()]
        print(f"Función: {func_name}, Argumentos: {args}")  # Depuración

        # Verificar si algún argumento es None
        if any(arg is None for arg in args):
            print(f"❌ Error: Argumentos inválidos para {func_name}: {args}")
            return None

        # Convertir nombres de columna en sus valores
        for i in range(len(args)):
            if isinstance(args[i], str) and args[i] in self.data.columns:
                args[i] = self.data[args[i]]

        resultado = None

        if func_name == 'suma':
            resultado = args[0].sum()
        elif func_name == 'promedio':
            resultado = args[0].mean()
        elif func_name == 'mediaPonderada':
            resultado = (args[0] * args[1]).sum() / args[1].sum()
        elif func_name == 'desviacion':
            resultado = args[0].std()
        elif func_name == 'mediana':
            resultado = args[0].median()
        elif func_name == 'varianza':
            resultado = args[0].var()
        else:
            print(f"❌ Función no soportada: {func_name}")
            return None

        print(f"✅ Resultado de {func_name}: {resultado}")

        # Verificar si el resultado es None antes de devolverlo
        if resultado is None:
            print(f"❌ Error: La función {func_name} devolvió None.")
            return None

        return float(resultado)


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
        print(f"📂 Leyendo archivo: {file_path}")  # 🚀 Depuración

        with open(file_path, 'r') as file:
            content = file.read()
            print(f"📄 Contenido del archivo:\n{content}")  # 🚀 Verificar si el archivo tiene datos

            input_stream = InputStream(content)

        lexer = FormulaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FormulaParser(stream)

        print("⚡ Ejecutando parser...")  # 🚀 Depuración antes de procesar
        tree = parser.file_()  # 🔹 Ahora usamos `file_()` en lugar de `file()`

        # 🌳 Imprimir el árbol sintáctico
        print("\n🌳 Árbol sintáctico generado:")
        print(tree.toStringTree(recog=parser))  # 🔥 Imprime el árbol en formato string

        print("🌳 Árbol sintáctico construido, iniciando visitor...")  # 🚀 Depuración
        results = visitor.visit(tree)

        print(f"✅ Resultados obtenidos: {results}")  # 🚀 Mostrar resultados
        return results

    except Exception as e:
        print(f"❌ Error al procesar las fórmulas: {e}")
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
