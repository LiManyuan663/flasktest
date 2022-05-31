from flask import Flask, request
import json
from examples import base_demo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello manyuan!'

@app.route('/sim',methods=['POST'])
def selectSim():
    print("开始读取数据了")
    data = request.get_data()
    data = json.loads(data)
    input=[]
    input.append(data['text'])
    print(input)
    # result={}
    # result['document']=base_demo.selectSim1(input)
    # result['case']=base_demo.selectSim2(input)
    return base_demo.selectSim2(input)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    app.run()
