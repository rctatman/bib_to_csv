from pybtex.database.input import bibtex
import string

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("bibliography.bib")

# tralsator for removing punctuation
translator = str.maketrans('', '', string.punctuation)

# open our output file
f = open('my_bib.csv', 'w') 

# header row
f.write("title\t year\t author\t journal\n")

#loop through the individual references
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
        # change these lines to create a SQL insert
        f.write(b["title"])
        f.write(" \t")
        f.write(b["year"])
        f.write(" \t")
        #deal with multiple authors
        authors = ""
        for author in bibdata.entries[bib_id].persons["author"]:
            new_author = str(author.first()) + " " + str(author.last()) 
            new_author = new_author.translate(translator)
            if len(authors) == 0:
                authors = '"' + new_author
            else:
                authors = authors + ", " + new_author
        f.write(authors + '"')
        f.write(" \t")
        f.write(b["journal"])
    # field may not exist for a reference
    except(KeyError):
        f.write(b["booktitle"])
        f.write("\n")
        continue
    f.write("\n")
    
    # close output file
    f.close()
