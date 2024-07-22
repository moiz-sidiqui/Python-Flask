## Flask app Routing

from flask import Flask,render_template,request,redirect,url_for
#render_template library for html
#request library for knowing wether a request is GET or POST



#create a simple flask application

app=Flask(__name__)   #entry point of a program


#for making route(web pages)

#for homepage
@app.route('/', methods =['GET'] )                   #first arg is url
def welcome():   
    return "<h1>Welcome to the home Page!</h1>"               #Seconf arg is GET or POST




#for indexpage
@app.route('/index', methods =['GET'] )                  
def index():                                      #function name cannot be same
    return render_template('index.html')


#variable rule
#meaning of variable rule is that the variable 'score' has an explicit data type mentioned which is 'int'
@app.route('/success/<int:score>', methods=['GET'])   #success is url and score is the parameter the page will receive                 #the default is get method
def success(score):
    return 'The person has passed with the score:' + str(score)


@app.route('/fail/<int:score>', methods=['GET'])   #success is url and score is the parameter the page will receive                 #the default is get method
def fail(score):
    return 'The person has failed with the score:' + str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)


if __name__ == '__main__':
    app.run(debug=True)  # if it is True then I dont need to stop server whenever I need to make a change in the code

    #app.run takes two information:
    #defaul URL is localhost and default port is 5000