Tutorial
===================

Firstly, you instantiate a new :class:`HTML5Builder`:

    >>> from html5builder import HTML5Builder
    >>> tag = HTML5Builder()


With this instance, you can output the string of an element:

    >>> str(tag.br())
    '<br>'

As the first argument, you can put the inner text of an element:

    >>> str(tag.h1('header'))
    '<h1>header</h1>'

When you want to build a blank element,
put a blank string in the first argument:

    >>> str(tag.div(''))
    '<div></div>'


With keyword arguments, you can specify the attribures of an element:

    >>> str(tag.img(src='image.jpg', alt='image'))
    '<img src="image.jpg" alt="image">'

When you want to specifiy the `class` attribute of an element,
use `cls` instead of `class`:

    >>> str(tag.div(cls='main'))
    '<div class="main">'


You can nest elements by passing an element in the first argument:

    >>> str(tag.a(tag.img(src='image.jpg'), href='target.html'))
    '<a href="target.html"><img src="image.jpg"></a>'

With a list as the first argument,
you can put multiple children into an element:

    >>> str(tag.a([tag.img(src='image.jpg'), 'link'], href='target.html'))
    '<a href="target.html"><img src="image.jpg">link</a>'


The following code generates a whole HTML5 document:

    >>> tag.doctype + str(
    ...     tag.html([tag.head(tag.title('title')), tag.body('body')]))
    '<!DOCTYPE html><html><head><title>title</title></head><body>body</body></html>'


A method call of the builder returns an instance of :class:`HTML5Element`:

    >>> tag.a('link', href='target.html')
    HTML5Element('a', ['link'], {'href': 'target.html'})

Through ``child`` and ``attrs`` attributes of :class:`HTML5Element`,
you can access and manipulate the children and attributes:

    >>> anchor = tag.a('link', href='target.html')
    >>> anchor.child
    ['link']
    >>> anchor.attrs
    {'href': 'target.html'}

You can also use a syntax sugar to access attributes:

    >>> anchor['href'] = 'new_target.html'
    >>> anchor['href']
    'new_target.html'
