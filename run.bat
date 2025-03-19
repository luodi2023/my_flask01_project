@echo off 

call myvenv01\Scripts\activate

flask --app flasky:create_app('default') run --debug

