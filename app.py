from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def binary_to_decimal(binary):
    return int(binary, 2)

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        binary_input1 = request.form['binary_input1']
        binary_input2 = request.form['binary_input2']
        
        try:
            if len(binary_input1) != 8 or len(binary_input2) != 8:
                return render_template('index.html', error_message="Please enter 8-bit binary numbers")
            
            decimal_output1 = binary_to_decimal(binary_input1)
            decimal_output2 = binary_to_decimal(binary_input2)
            
            addition_result = decimal_output1 + decimal_output2
            
            return render_template('index.html', 
                                   decimal_output1=decimal_output1, 
                                   decimal_output2=decimal_output2, 
                                   addition_result=addition_result)
        
        except ValueError:
            return render_template('index.html', error_message="Please enter valid binary numbers")

if __name__ == '__main__':
    app.run(debug=True)
