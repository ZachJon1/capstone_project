import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor('xception', target_size=(150, 150))

interpreter = tflite.Interpreter(model_path='model_X.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

#url = 'https://raw.githubusercontent.com/ZachJon1/capstone_project/main/img/test_1.jpg?token=AOGFKC6YCRCGNT5L6RFTCITBWR44G'

def predict(url):
    X = preprocessor.from_url(url)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    pred = interpreter.get_tensor(output_index)
    float_pred =  pred.tolist()


    return (float_pred)



def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
