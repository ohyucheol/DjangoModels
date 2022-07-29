# DjangoApps

가상환경(venv)활성화(path/venv)
	. bin/activate

프로젝트폴더(project) 생성 및 진입(path/to/venv)
	mkdir project
	cd project

장고 프로젝트(main) 생성(path/to/venv/project)
	django-admin startproject main .

장고 앱 폴더(DjangoApp) 생성 및 진입(path/to/venv/project), __init__.py 생성(path/to/venv/project/DjangoApp)
	mkdir project DjangoApp
	cd DjangoApp
	touch __init__.py

원하는 앱(u01) 생성(path/to/venv/project/DjangoApp)
	python3 ../manage.py startapp u01

이후 앱의 apps.py에서 앱 이름(name='u01')을 name='DjangoApps.u01'로 변경(path/to/venv/project/DjangoApp/u01/apps.py)
	class U01Config(AppConfig):
		default_auto_field = 'django.db.models.BigAutoField'
		name = 'DjangoApps.u01'

장고 프로젝트의 settings.py에 INSTALLED_APP 설정(path/to/venv/project/main/settings.py)
	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'DjangoApps.u01.apps.U01Config',
	]