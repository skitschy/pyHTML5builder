import unittest

import html5builder


class TestHTML5Element(unittest.TestCase):
    def test_init_strchild(self):
        element = html5builder.HTML5Element(
            'name', 'inner_text', {'attr': 'avalue'})
        self.assertEqual(element.name, 'name')
        self.assertEqual(element.child, ['inner_text'])
        self.assertEqual(element.attrs, dict(attr='avalue'))

    def test_init_singlechild(self):
        child = html5builder.HTML5Element('child', (), {})
        element = html5builder.HTML5Element(
            'name', child, {'attr': 'avalue'})
        self.assertEqual(element.name, 'name')
        self.assertEqual(element.child, [child])
        self.assertEqual(element.attrs, dict(attr='avalue'))

    def test_init_listchild(self):
        child = html5builder.HTML5Element('child', (), {})
        element = html5builder.HTML5Element(
            'name', ['text1', child, 'text2'], {'attr': 'avalue'})
        self.assertEqual(element.name, 'name')
        self.assertEqual(element.child, ['text1', child, 'text2'])
        self.assertEqual(element.attrs, dict(attr='avalue'))

    def test_getitem(self):
        element = html5builder.HTML5Element('name', (), {'attr': 'avalue'})
        self.assertEqual(element['attr'], 'avalue')

    def test_setitem(self):
        element = html5builder.HTML5Element('name', (), {})
        self.assertEqual(element.attrs, {})
        element['attr'] = 'avalue'
        self.assertEqual(element.attrs, dict(attr='avalue'))

    def test_str(self):
        element = html5builder.HTML5Element(
            'name', 'inner_text', {'attr': 'avalue'})
        self.assertEqual(str(element), '<name attr="avalue">inner_text</name>')

    def test_str_noattr(self):
        element = html5builder.HTML5Element('name', 'inner_text', {})
        self.assertEqual(str(element), '<name>inner_text</name>')

    def test_str_emptychild(self):
        element = html5builder.HTML5Element('name', '', {'attr': 'avalue'})
        self.assertEqual(str(element), '<name attr="avalue"></name>')

    def test_str_nochild(self):
        element = html5builder.HTML5Element('name', (), {'attr': 'avalue'})
        self.assertEqual(str(element), '<name attr="avalue">')

    def test_str_listchild(self):
        child = html5builder.HTML5Element('child', (), {})
        element = html5builder.HTML5Element(
            'name', ['text1', child, 'text2'], {'attr': 'avalue'})
        self.assertEqual(str(element),
                         '<name attr="avalue">text1<child>text2</name>')


class TestHTML5Builder(unittest.TestCase):
    def test_getattr(self):
        tag = html5builder.HTML5Builder()
        self.assertEqual(str(tag.name('inner_text', attr='avalue')),
                         '<name attr="avalue">inner_text</name>')

    def test_getattr_nochild(self):
        tag = html5builder.HTML5Builder()
        self.assertEqual(str(tag.name(attr='avalue')), '<name attr="avalue">')

    def test_getattr_noattr(self):
        tag = html5builder.HTML5Builder()
        self.assertEqual(str(tag.name('inner_text')), '<name>inner_text</name>')


if __name__ == '__main__':
    unittest.main()
