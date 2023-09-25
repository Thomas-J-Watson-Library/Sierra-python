#!Python
# file: expOUTPUT.py
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# desc: The functions in this script generate and HTML page on the fly
#       The page uses the bootstrap style of 12 column grid layout. Function
#       'make_404_page' generates a complete file, whereas the other functions
#       generate a specific segment of the page.
# use:  The functions in this script are called from explorer.py
#
def make_404_page(id):
    from datetime import datetime
    now = datetime.now()
    #
    H0 =  '<!DOCTYPE html>'
    H0 += '<html lang="en">'
    H0 += '<head>'
    H0 += '<title>TJWL Data Explorer Error</title>'
    H0 += '<meta charset="utf-8">'
    H1  = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    H1 += '<meta author="Michael Cummings, Library Systems">'
    H1 += '<meta name="generator" content="Python">'
    H1 += '<meta name="description" content="Information from APIs and URIs for a given bib record">'
    H1 += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">'
    H1 += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>'
    H1 += '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">'
    H1 += '</head>'
    H1 += '<body>'
    A1 =  '<div class="container p-3 my-3   "><div >'
    A1 += '   <div class="col-sm-12 bg-danger text-white"><class="display-6">'
    A1 += '      <h3> &nbsp; Data Explorer</h3>'
    A1 += '       &nbsp; &nbsp; <strong>Thomas J Watson Library</strong><br/>'
    A1 += '       &nbsp; &nbsp; The Metropolitan Museum of Art'
    A1 += '      <br/><br/> </div> </div>'
    A1 += '  <div class="accordion" id="accordionTJWL">'
    A1 += '    <h2 class="accordion-header" id="headingOne">'
    A1 += '      <button class="accordion-button" type="button" data-bs-toggle="collapse"'
    A1 += '      data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">'
    A1 += '        <div class="row">'
    A1 += '             <div class="col-sm-12"><class="display-6">'
    A1 += '              <h3><i class="bi-exclamation-triangle"></i> &nbsp; '
    A1 += id
    A1 += '     not found</h3> </div>'
    A1 += '       </div>    </h2>'
    A1 += '    <div id="collapseOne" class="accordion-collapse collapse"'
    A1 += '    aria-labelledby="headingOne"  data-bs-parent="#accordionTJWL">'
    A1 += '      <div class="accordion-body">'
    A1 += '        <div class="row">'
    A1 += '            <div class="col-sm-12">'
    A1 += '            The program was unable to find a bib matching the value you'
    A1 += '            requested.'
    A1 += '        </div>'
    A1 += '    </div> <!-- end accordion body -->'
    A1 += '  </div> <!-- collapseOne  -->'
    A1 += '</div> <!-- accordion item -->'
    A1 += '</div> <!-- end accordionTJWL         -->'
    A1 += '</div> <!-- end container p-3 my-3    -->'
    FT  = '<!-- footer -->'
    FT += ' <div class="container p-3 my-3   ">'
    FT += '<div >'
    FT += '<div class="col-sm-12" ><class="display-6">'
    FT += '  <p class="text-muted">'
    FT += '  Data Explorer Bib Error | Rev 0-060722 | Page generated '
    FT += str(now)
    FT += '</p></div></div><!-- end footer --></body></html>'
    #
    #
    OUTF= open('404.html', 'w')
    print(H0, file=OUTF)
    OUTF.close()
    OUTF= open('404.html', 'a')
    print(H1, file=OUTF)
    print(A1, file=OUTF)
    print(FT, file=OUTF)
    OUTF.close()

#-------------------------------------#
# functions for specific sections     #
#-------------------------------------#
def make_head(id):
    from datetime import datetime
    now = datetime.now()
    #
    H0 =  '<!DOCTYPE html>'
    H0 += '<html lang="en">'
    H0 += '<head>'
    H0 += '<title>TJWL Data Explorer : bib .b'
    H0 += str(id)
    H0 += 'a </title>'
    H0 += '<meta charset="utf-8">'
    H1  = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    H1 += '<meta author="Michael Cummings, Library Systems">'
    H1 += '<meta name="generator" content="Python">'
    H1 += '<meta name="description" content="Information from APIs and URIs for a given bib record">'
    H1 += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">'
    H1 += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>'
    H1 += '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">'
    H1 += '</head>'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'w')
    print(H0, file=OUTF)
    OUTF.close()
    OUTF= open(htmlpage, 'a')
    print(H1, file=OUTF)
    OUTF.close()

def make_body_to_sierra(id):
    B0  = '<body><div class="container p-3 my-3   ">'
    B0 += '<div>'
    B0 += '<div class="col-sm-12 bg-primary text-white"><class="display-6">'
    B0 += '<h3> &nbsp; Data Explorer</h3>'
    B0 += '   &nbsp; &nbsp; <strong>Thomas J Watson Library</strong><br/>'
    B0 += '   &nbsp; &nbsp; The Metropolitan Museum of Art <br/><br/>'
    B0 += '</div></div>'
    B1 =  '<div class="accordion" id="accordionTJWL">'
    B1 += '<div class="accordion-item">'
    B1 += '<h2 class="accordion-header" id="headingOne">'
    B1 += '<button class="accordion-button" type="button" data-bs-toggle="collapse"'
    B1 += ' data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">'
    B1 += ' <div class="row">'
    B1 += ' <div class="col-sm-12"><class="display-6">'
    B1 += ' <h3><i class="bi-book"></i>'
    B1 += '  Bib Record .b' + id + 'a </h3> </div>'
    B1 += ' </div> </h2>'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(B0, file=OUTF)
    print(B1, file=OUTF)
    OUTF.close()

def make_bibinfo(id):
    I0  = ' <div id="collapseOne" class="accordion-collapse collapse"'
    I0 += ' aria-labelledby="headingOne"  data-bs-parent="#accordionTJWL">'
    I0 += '<div class="accordion-body">'
    I0 += '<div class="row">'
    I0 += '<div class="col-sm-4"><class="display-6">'
    I0 += '<h3><i class="bi-book"></i> Summary</h3>'
    I0 += '</div>'
    I0 += '<div class="col-sm-8"><a href="https://library.metmuseum.org/search~S1?/.b'
    I0 += id + '/.b' + id +'/1%2C1%2C1%2CB/marc~b' + id + '"'
    I0 += 'target="_new">'
    I0 += '<button type="button" class="btn btn-primary btn-sm">WatsonLine b'
    I0 += id + ' MARC</button></a> </div>  </div>'
    I0 += '<!-- OUTPUT KEY AND VALUE FROM Sierra list -->'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(I0, file=OUTF)
    OUTF.close()

def make_iteminfo(id):
    M2 =  ' <div class="accordion-item">'
    M2 += '<h2 class="accordion-header" id="headingTwo">'
    M2 += '<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" '
    M2 += ' data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">'
    M2 += '<div class="row"><div class="col-sm-12"><class="display-6">'
    M2 += '<h3><i class="bi-upc"></i> Item Details</h3> </div></div></button></h2>'
    M2 += '<div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" '
    M2 += ' data-bs-parent="#accordionTJWL">'
    M2 += '<div class="accordion-body">'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(M2, file=OUTF)
    OUTF.close()

def make_namesinfo(id):
    N3 = '<div class="accordion-item">'
    N3 += '<h2 class="accordion-header" id="headingThree">'
    N3 += '  <button class="accordion-button collapsed" type="button" '
    N3 += '  data-bs-toggle="collapse" data-bs-target="#collapseThree" '
    N3 += '  aria-expanded="false" aria-controls="collapseThree">'
    N3 += '    <div class="row">'
    N3 += '          <div class="col-sm-12"><class="display-6">'
    N3 += '          <h4><i class="bi bi-share"></i> Linked Data</h4>'
    N3 += '        </div>'
    N3 += '    </div>'
    N3 += '  </button>'
    N3 += '</h2>'
    N3 += '<div id="collapseThree" class="accordion-collapse collapse "'
    N3 += ' aria-labelledby="headingThree" data-bs-parent="#accordionTJWL">'
    N3 += '  <div class="accordion-body">'
    N3 += '   <div class="row">'
    N3 += '        <div class="col-sm-4">'
    N3 += '        <h4><i class="bi bi-person-check"></i> &nbsp; Information from Name URIs '
    N3 += '        </div>'
    N3 += '        <div class="col-sm-8">http://id.loc.gov/authorities/names/</div>'
    N3 += '        </h4>'
    N3 += '    </div>'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(N3, file=OUTF)
    OUTF.close()

def make_subjectsinfo(id):
    S3 = '<div class="row">'
    S3 += ' <div class="col-sm-12"> &nbsp; </div>'
    S3 += '  </div>'
 #   S3 += '  </div>'
    S3 += '  <div class="row">'
    S3 += '      <div class="col-sm-4">'
    S3 += '      <h4><i class="bi bi-folder2-open"></i> &nbsp;  Information from Subject URIs</h4></div>'
    S3 += '      <div class="col-sm-8">'
    S3 += '            http://id.loc.gov/authorities/subjects/</div>'
    S3 += '  </div>  '
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(S3, file=OUTF)
    OUTF.close()

def make_external(id):
    M2 =  ' <div class="accordion-item">'
    M2 += '<h3 class="accordion-header" id="headingFour">'
    M2 += '<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" '
    M2 += ' data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">'
    M2 += '<div class="row"><div class="col-sm-12"><class="display-6">'
    M2 += '<h3><i class="bi-globe"></i> External APIs</h3> </div></div></button></h3>'
    M2 += '<div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" '
    M2 += ' data-bs-parent="#accordionTJWL">'
    M2 += '<div class="accordion-body">'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(M2, file=OUTF)
    OUTF.close()

def make_oclcinfo(id):
    X1 = '<div class="row">'
    X1 += ' <div class="col-sm-12"> &nbsp; </div>'
    X1 += '  </div>'
    X1 += '  <div class="row">'
    X1 += '      <div class="col-sm-4">'
    X1 += '      <h4><i class="bi bi-building"></i> &nbsp;  OCLC Local Holdings API</h4></div>'
    X1 += '      <div class="col-sm-8">'
    X1 += '            http://www.worldcat.org/webservices (10025, up to 50 libraries)</div>'
    X1 += '  </div>  '
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(X1, file=OUTF)
    OUTF.close()

def make_openlibrary(id):
    X1 = '<div class="row">'
    X1 += ' <div class="col-sm-12"> &nbsp; </div>'
    X1 += '  </div>'
    X1 += '  <div class="row">'
    X1 += '      <div class="col-sm-4">'
    X1 += '      <h4><i class="bi bi-image"></i> &nbsp;  Open Library Image API</h4></div>'
    X1 += '      <div class="col-sm-8">'
    X1 += '            http://covers.openlibrary.org/b/isbn/</div>'
    X1 += '  </div>  '
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(X1, file=OUTF)
    OUTF.close()

def make_data_row(id, tag, label, data):
    # print('receiving',id,tag,label,data)
    if data == None:
        data = 'NULL'
    D0 = '<div class="row">'
    D0 += '<div class="col-sm-1">' + tag   + '</div>'
    D0 += '<div class="col-sm-3">' + label + '</div>'
    D0 += '<div class="col-sm-8">' + '&nbsp; ' + data  + '</div></div>'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a', encoding='utf-8')
    print(D0, file=OUTF)
    OUTF.close()

def make_cover(id, isbn):
    CI = '<div class="row">'
    CI += '<div class="col-sm-1"> &nbsp; </div>'
    CI += '<div class="col-sm-3">Cover Image</div>'
    CI += '<div class="col-sm-8"><img src="http://covers.openlibrary.org/b/isbn/' + isbn
    CI += '-L.jpg" class="img-fluid" alt="Responsive image"></div></div>'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a', encoding='utf-8')
    print(CI, file=OUTF)
    OUTF.close()

def make_end_accordion_item(id):
    EA0  = '<div class="row" > <div class="col-sm-1"> &nbsp; </div>'
    EA0 += '<div class="col-sm-3"> &nbsp; </div><div class="col-sm-8"> &nbsp; </div>'
    EA0 += '</div></div> <!-- end accordion body -->'
    EA0 += '</div> <!-- collapse  -->'
    EA0 += '</div> <!-- accordion item -->'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(EA0, file=OUTF)
    OUTF.close()

def make_footer(id):
    from datetime import datetime
    now = datetime.now()
    F0 = '<!-- footer -->'
    F0 += '</div></div><div class="container p-3 my-3   ">'
    F0 += '<div > <div class="col-sm-12" ><class="display-6">'
    F0 += ' <p class="text-muted"> Data Explorer | Rev A-083122 | Page generated '
    F0 += str(now) + ' </p> </div> </div><!-- end footer --></body></html>'
    htmlpage = 'b' + id  + 'a.html'
    OUTF= open(htmlpage, 'a')
    print(F0, file=OUTF)
    OUTF.close()
