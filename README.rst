What
=====

This is a decorator for a django view that will request Basic Authentication.
This is a copy of https://djangosnippets.org/snippets/243/

Why
====

There are serveral reasons for this Package:

  * I wanted Basic Authentication for just a couple of views. So the RemoteUserAuthBackend was no option. Also I did not want to configure the webserver to do Basic Authentication.
  * As you can read in the comments of https://djangosnippets.org/snippets/243/ there are some bugs in it - so I wanted to have them fixed - but also documented that they were fixed and in the end provide a fixed version of it
  * Also I just want to install it via pip

How to use
===========

Apache
-------

Add this to your apache config to tell apache to pass the Authorication Headers to your application:

  WSGIPassAuthorization On

Django
-------

Function Views
################

.. code::

  @logged_in_or_basicauth()
  def view(request):
      return 'Hello World.'

Class based Views
##################

Django 1.8

.. code::

  class View(TemplateView):
      template_name = 'hello.html'

      @method_decorator(logged_in_or_basicauth())
      def dispatch(self, *args, **kwargs):
          return super(View, self).dispatch(*args, *kwargs)

Django 1.9: method_decorator now works on classes: 

.. code::

  @method_decorator(logged_in_or_basicauth(), name='dispatch')
  class View(TemplateView):
      template_name = 'hello.html'
