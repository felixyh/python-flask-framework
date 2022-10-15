from werkzeug.serving import run_simple

def func(environ, start_response):
    print('request is coming!')
    pass
    
if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, func)