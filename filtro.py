#!/usr/bin/env python

from panflute import run_filter, CodeBlock

def action(elem, doc):
    if isinstance(elem, CodeBlock):
        #print(elem)
        if 'linenums' in elem.classes:
            elem.attributes['numberLines'] = 'true'
            if 'linenums' in elem.attributes:
                elem.attributes['startFrom'] = elem.attributes['linenums']
            elem.classes.remove('linenums')

def main(doc=None):
    run_filter(action, doc=doc)

if __name__ == "__main__":
    main()