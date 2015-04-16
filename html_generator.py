def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML=''
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

LIST_OF_CONCEPTS1 = [ ['Computers', 'Computers are awesome. They are universal machines that can be used to solve problems'],
                             ['Computer language', 'Artificial languages that permits us interact with computers'],
                             ['Computers and lazyness', 'Computers, different than humans, are not lazy!'] ]
 
print make_HTML_for_many_concepts(LIST_OF_CONCEPTS1)











