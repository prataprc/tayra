Tayra templating is a full-featured abstract markup language to describe
web-documents. It is primarily inspired from
`mako-template <http://www.makotemplates.org/>`_ and 
`HAML <http://haml-lang.com/>`_ (especially the indentation based
markup definitions). Although it is young and relatively a new kid among
the old-timers, it can be considered as the evolutionary next step for some of
them. And probably it is the only templating language that allows developers
to build and distribute their templates as plugins, not to mention the fact
that tayra's implementation itself is heavily based on plugins.
    
Why templating at-all
---------------------

Those who are new to web-app development could be wondering why to template
html ? If need be, why not use one of the many dynamic languages (given the
fact that most of the web-apps are written using one of them) to directly
generate the dynamic parts of a web document ?

* Composing HTML via a programming language (like, python, php, ruby) can be
  more cumbersome and could involve more coding. By the time the developer is
  satisfied with the web page, it would have gone through dozens of trial.
  A templating language is supposed to help developers focus on the look and
  feel (sometimes function) of the document and less on programming it.
* Expression substitution, is probably the main feature which allows dynamic
  content to be substituted inside a template.
* Template re-use by abstracting them into function blocks.
* Many popular templating language supports control blocks like, if-else,
  and for/while loops.

Welcome to Tayra
----------------

The objective of tayra templating is to create concise, beautiful and highly
re-usable HTML templates for web. Although it is fairly in the beginning
stage, we hope it has succeeded in solving many problems towards that end. To
get you started, here is a non-exhaustive list of features and functions
available from tayra.

``expression substitution``,
  Substitute dynamic content anywhere in your document using python expression.

``escaping text``,
  While substituting text, it can be escaped with one or more filters. While
  escape-filters themselves can be added as plugins to tayra.

``filter blocks``,
  Process non-template text and substitute the filter block with
  processed text (optional). One such example can be a block of python code
  that need to do some `view` related processing. And of course one can 
  create any many types of filter-blocks (plugins !!)

``control blocks``,
  Make use of control blocks like ``if-elif-else``, to conditionally select
  portions of templates. And ``for/while`` loop to repeat blocks of template
  text.

``functions``,
  Abstract re-usable blocks of templates into functions with its own local
  scope and local-context.

``import templates``,
  Import templates from other parts of the source tree into the current
  template's namespace and access their function blocks.

``inheritance``,
  There is a simple yet powerful idea of inheritance, whereby templates
  can have a long chain of inheritance from the base layout. A template
  module in the chain can access any other inheriting or inherited templates
  using the ``parent`` and ``next`` namespace, while ``this`` namespace
  provides you the magic of overriding.

``how to use``,
  Can be used via its well-defined API or from command line.

Template plugins
----------------

Tayra is probably the only templating language that enable developers to build
and distribute templates as plugins, based on well defined specification and
distribute them as packages. And others who would like to use them can simply
query for their interface and consume their templates. Now, this one feature
will ensure that developers can finally get a plugin architecture without
compromising their MVC design pattern, not a bit.

**Implementation philosopy**

Tayra templating engine itself is nothing but a specification of syntax
spun around a collection of plugin framework. And advanced users
may find it exiting that, they can change and extend the behavior
(to some extent even the syntax) of the template language. Fact is, tayra
cannot even parse simple html tags by itself. Fortunately a 'html5'
collection of plugins are shipped with the package, that can interpret the
standard html tags and generate the html-text for you.

But personally I would love to do tayra-templating just for the way the 
template code looks - concise and beautiful (thanks to HAML).

**A note on implementation philosopy**

- The templating engine itself is nothing but a specification of syntax
  spun around a collection of plugin framework. And advanced users may find it
  exiting that they can change and extend the behavior (to some extent even the
  syntax) of the template language. Fact is, tayra cannot even parse simple
  html
  tags by itself.

- All programmable expressions, statements and other language-like concepts
  are nothing but pure python, wrapped inside convenient syntax.

- TTL (Tayra Template Language) files are compiled into python text containing
  stack-machine instructions, interpreted using a stack machine object.

- Almost every aspect of language functionalities (except the programmable
  parts) are extensible via plugins.

- But personally I would love to do tayra-templating just for the way the 
  template code looks - concise and beautiful (thanks to HAML).
