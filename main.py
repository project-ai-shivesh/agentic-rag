
from dotenv import load_dotenv
load_dotenv()
from graph.graph import app

if __name__ == '__main__':
    print('Hello From Corrective RAG!')
    print(app.invoke(input={"question":"what is memory agent"}))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
