# tacl_submission (official_transacl_finalversion_formatting_pdf)

Source URL: https://transacl.org/tacl-submission-templates/tacl2021v1-finalversion-formatting-instructions.pdf
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/tacl_submission/official_transacl_finalversion_formatting_pdf_tacl2021v1-finalversion-formatting-instructions.pdf.pdf`

## Page 1

Formatting Instructions for TACL Final Versions
(Base files: tacl2021v1-template.tex & tacl2021v1.sty, dated Dec. 15, 2021)
Template Author1∗
Template Affiliation1/Address Line 1
Template Affiliation1/Address Line 2
Template Affiliation1/Address Line 2
template.email1example.com
Template Author2
Template Affiliation2/Address Line 1
Template Affiliation2/Address Line 2
Template Affiliation2/Address Line 2
template.email2@example.com
Abstract
This document contains the formatting re-
quirements for TACL final versions. These
formatting rules take effect for all final ver-
sions received from September 2, 2018 on-
wards.
1
Courtesy warning: Common violations
of final version rules that have resulted
in papers being returned to authors for
corrections
Avoid publication delays by avoiding these.
1. Violation: incorrect parentheses for in-text
citations. See §10.1 and Table 3.
2. Violation: URLs that, when clicked, yield an
error such as a 404 or go to the wrong page.
• Advice: best scholarly practice for ref-
erencing URLS would be to also include
the date last accessed.
3. Violation: non-fulfillment of promise from
submission to provide access instructions
(such as a URL) for code or data.
4. Violation: References incorrectly formatted
(see §10.2). Specifically:
(a) Violation:
initials
instead
of
full
first/given names in references.
(b) Violation: missing periods after middle
initials.
(c) Violation: incorrect capitalization. For
example, change “lstm” to LSTM and
“glove” to GloVe.
• Advice: if using BibTex, apply curly
braces within the title field to pre-
serve intended capitalization.
∗The actual contributors to this instruction document
and corresponding template file are given in Section 13.
(d) Violation: using “et al.” in a reference
instead of listing all authors of a work.
• Advice: List all authors and check
accents on author names even when
dozens of authors are involved.
(e) Violation: not giving a complete arXiv
citation number.
• Advice:
best scholarly practice
would be to give not only the full
arXiv number, but also the version
number, even if one is citing version
1.
(f) Violation: not citing an existing peer-
reviewed version in addition to or in-
stead of a preprints
• Advice:
When
preparing
the
camera-ready, perform an additional
check of preprints cited to see
whether a peer-reviewed version has
appeared in the meantime.
(g) Violation: book titles do not have the
first initial of all main words capitalized.
(h) Violation: In a title, not capitalizing the
first letter of the first word after a colon
or similar punctuation mark.
5. Violation: figures or tables appear on the first
page.
6. Violation: the author block under the title is
not formatted according to Appendix A.
2
General instructions
Final versions that do not comply with this doc-
ument’s instructions risk publication delays until
the camera-ready is brought into compliance.
Final versions should consist of a Portable Doc-
ument Format (PDF) file formatted for A4 paper.1
All necessary fonts should be included in the file.
1Prior to the September 2018 submission round, a differ-
ent paper size was used.

## Page 2

Note that you will need to provide both a single-
spaced and a double-spaced version; see §6.
If you promised to provide code or data at sub-
mission, specific instructions for how to access
such resources must be provided.
(Typically, a
URL to a stable, resource-specific site suffices.)
All URLs should be manually checked to verify
that they lead to a valid webpage, and to the site
that was intended.
3
LATEX files
LATEX files compliant with these instructions are
available at the Author Guidelines section of
the
TACL
website,
https://www.transacl.org.2
Use of the TACL LATEX files is highly rec-
ommended:
MIT Press requires authors to
supply LATEX source files as part of the publi-
cation process; and use of the recommended
LATEX files makes conversion to the required
camera-ready format simple.
Specifically, the
conversion can be accomplished by as little as:
(1) add “acceptedWithA” in the square brackets
in the line invoking the TACL package, like so:
\usepackage[acceptedWithA]{tacl2021v1}
(2) add author information; (3) add acknowledg-
ments.
3.1
Workarounds for problems with the
hyperref package
The provided files use the hyperref package by de-
fault. The TACL files employs the hyperref pack-
age to make clickable links for URLs and other
references, and to make titles of bibliographic
items into clickable links to their DOIs in the gen-
erated pdf.3
However,
it
is
known
that
citations
or
URLs that cross pages can trigger the com-
pilation
error
“\pdfendlink ended up
in different nesting level than
\pdfstartlink”.
In such cases, you may
temporarily disable the hyperref package and then
compile to locate the offending portion of the tex
file; edit to avoid a pagebreak within a link;4 and
then re-enable the hyperref package.
2Last accessed Dec. 15, 2021.
3Indeed, for some versions of acl_natbib.sty, DOIs and
URLs are not printed out or included in the bibliography in
any form if the hyperref package is not used.
4If the problematic link is part of a reference in the
bibliography and you do not wish to directly edit the
corresponding .bbl file, a heavy-handed approach is to add
the line \interlinepenalty=10000 just after the line
\sloppy\clubpenalty4000\widowpenalty4000
Type of Text
Size
Style
paper title
15 pt
bold
author names
12 pt
bold
author affiliation
12 pt
the word “Abstract” as header
12 pt
bold
abstract text
10 pt
section titles
12 pt
bold
document text
11 pt
captions
10 pt
footnotes
9 pt
Table 1: Font requirements
To disable it, add nohyperref in the square
brackets to pass that option to the TACL pack-
age. For example, change [acceptedWithA]
in \usepackage[acceptedWithA]{tacl2021v1}
to [acceptedWithA,nohyperref].
4
Length limits
Camera-ready documents may consist of as many
pages of content as allowed by the Action Editor
in their final acceptance letter.
The page limit includes any appendices. How-
ever, references and acknowledgments do not
count toward the page limit.
5
Fonts and text size
Adobe’s Times Roman font should be used.
In LATEX2e this is accomplished by putting
\usepackage{times,latexsym}
in
the
preamble.5
Font size requirements are listed in Table 1. In
addition to those requirements, the content of fig-
ures, tables, equations, etc. must be of reasonable
size and readability.
6
Page Layout
The margin dimensions for a page in A4 format
(21 cm × 29.7 cm) are given in Table 2. Start the
content of all pages directly under the top margin.
Final versions must be in two-column format.
Allowed exceptions to the two-column format are
the title, which must be centered at the top of
the first page; the author block containing author
in the “\def\thebibliography” portion of the file
tacl2021v1.sty. This penalty means that LaTex will not allow
individual bibliography items to cross a page break.
5Should Times Roman be unavailable to you, use Com-
puter Modern Roman (LATEX2e’s default). Note that the latter
is about 10% less dense than Adobe’s Times Roman font.

## Page 3

Left and right margins: 2.5 cm
Top margin: 2.5 cm
Bottom margin: 2.5 cm
Column width: 7.7 cm
Column height: 24.7 cm
Gap between columns: 0.6 cm
Table 2: Margin requirements
names and affiliations and addresses, which must
be centered on the top of the first page and placed
after the title; The author names and affiliations
must be formatted according to MIT Press’s re-
quirements, which are described in Appendix A.
Using the provided LaTeX style file should satisfy
these requirments.
and any full-width figures or tables.
Should the pages be numbered? Yes, for sub-
missions (to facilitate review); but no, for camera-
readies (page numbers will be added at publication
time).
Final versions should be single-spaced.
But,
an additional double-spaced version must also
be provided, together with the single-spaced ver-
sion, for the use of the copy-editors. A double-
spaced version can be created by adding the
“copyedit” option: Change [acceptedWithA]
in \usepackage[acceptedWithA]{tacl2021v1}
to [acceptedWithA,copyedit].
Indent by about 0.4cm when starting a new
paragraph that is not the first in a section or sub-
section.
6.1
The confidentiality header and
line-number ruler
Camera-readies should not include the left- and
right-margin line-number rulers or headers from
the submission version.
The presence or absence of the ruler or header
should not change the appearance of any other
content on the page.
7
The First Page
Center the title, which should be placed 2.5cm
from the top of the page, and author names and
affiliations across both columns of the first page.
Long titles should be typed on two lines without
a blank line intervening. After the title, include
a blank line before the author block. Do not use
only initials for given names, although middle ini-
tials are allowed. Do not put surnames in all cap-
itals.6 Affiliations should include authors’ email
addresses. Do not use footnotes for affiliations.
Start the abstract at the beginning of the first
column, about 8 cm from the top of the page, with
the centered header “Abstract” as specified in Ta-
ble 1. The width of the abstract text should be nar-
rower than the width of the columns for the text in
the body of the paper by about 0.6cm on each side.
8
Section headings
Use numbered section headings (Arabic numerals)
in order to facilitate cross references. Number sub-
sections with the section number and the subsec-
tion number separated by a dot.
9
Figures and Tables
Place figures and tables in the paper near where
they are first discussed. Note that MIT Press dis-
allows figures and tables on the first page.
Provide a caption for every illustration. Num-
ber each one sequentially in the form: “Figure 1:
Caption of the Figure.” or “Table 1: Caption of the
Table.”
Authors should ensure that tables and figures do
not rely solely on color to convey critical distinc-
tions and are, in general, accessible to the color-
blind.
10
Citations and references
10.1
In-text citations
Use correctly parenthesized author-date citations
(not numbers) in the text. To understand correct
parenthesization, obey the principle that a sen-
tence containing parenthetical items should re-
main grammatical when the parenthesized mate-
rial is omitted. Consult Table 3 for usage exam-
ples.
10.2
References
Gather the full set of references together under the
boldface heading “References”. Arrange the ref-
erences alphabetically by first author’s last/family
name, rather than by order of occurrence in the
text.
References
to
peer-reviewed
publications
should be given in addition to or instead of
preprint versions. When giving a reference to a
preprint, including arXiv preprints, include the
number.
6Correct: “Lillian Lee”; incorrect: “Lillian LEE”.

## Page 4

Incorrect
Correct
“(Cardie, 1992) employed learning.”
“Cardie (1992) employed learning.”
The problem: “employed learning.” is not a sen-
tence.
Create by \citet{... } or \newcite{... }.
“The method of (Cardie, 1992) works.”
“The method of Cardie (1992) works.”
The problem: “The method of was used.” is not a
sentence.
Create as above.
“Use the method of (Cardie, 1992).”
“Use the method of Cardie (1992).”
The problem: “Use the method of.” is not a sen-
tence.
Create as above.
Related work exists Lee (1997).
Related work exists (Lee, 1997).
The problem: “Related work exists Lee.” is not a
sentence (unless one is scolding a Lee).
Create by \citep{... } or \cite{... }.
Table 3: Examples of incorrect and correct citation format. Also depicted are citation commands supported by the
tacl2018.sty file, which is based on the natbib package and supports all natbib citation commands. The tacl2018.sty
file also supports commands defined in previous ACL style files for compatibility.
List all authors of a given reference, even if
there are dozens; do not truncate the author list
with an “et al.” Use full first/given names for au-
thors, not initials. Include periods after middle ini-
tials.
Titles should have correct capitalization.
For
example, change “lstm” or “Lstm” to “LSTM”.7
Capitalize the first letter of the first word after a
colon or similar punctuation mark. For book titles,
capitalize the first letter of all main words. See the
reference entry for Jurafsky and Martin (2009) for
an example.
We strongly encourage the following, but do not
absolutely mandate them:
• Include DOIs.8
• Include the version number when citing
arXiv preprints, even if only one version ex-
ists at the time of writing. For example,9 note
the “v1” in the following.
7If using BibTex, apply curly braces within the title field
to preserve intended capitalization.
8The supplied LATEX files will automatically add hyper-
links to the DOI when BibTeX or BibLateX are invoked if
the hyperref package is used and the doi field is employed
in the corresponding bib entries. The DOI itself will not be
separately printed out in that case.
9Bibtex entries for Goodman (2001a) and Hwa (1999a)
corresponding to the depicted output can be found in the sup-
plied sample file tacl.bib. We also cite the peer-reviewed
versions (Goodman, 2001b; Hwa, 1999b), as required.
Joshua Goodman.
2001.
A bit
of progress in language modeling.
CoRR, cs.CL/0108005v1.
An alternative format is:
Rebecca Hwa. 1999. Supervised
grammar induction using training
data with limited constituent infor-
mation. cs.CL/9905001. Version 1.
11
Appendices
Appendices, if any, directly follow the text and the
references. Recall from Section 4 that appendices
count towards the page limit.
12
Including acknowledgments
Acknowledgments appear immediately before the
references. Do not number this section.10 If you
found the reviewers’ or Action Editor’s comments
helpful, consider acknowledging them.
13
Contributors to this document
This document was adapted by Lillian Lee and
Kristina Toutanova from the instructions and files
for ACL 2018, by Shay Cohen, Kevin Gimpel, and
Wei Lu. This document was updated by Cindy
10In
LATEX,
one
can
use
\section*
instead
of
\section.

## Page 5

Robinson to include additional information on for-
matting final versions.
Those files were drawn
from earlier *ACL proceedings, including those
for ACL 2017 by Dan Gildea and Min-Yen Kan,
NAACL 2017 by Margaret Mitchell, ACL 2012 by
Maggie Li and Michael White, those from ACL
2010 by Jing-Shing Chang and Philipp Koehn,
those for ACL 2008 by Johanna D. Moore, Si-
mone Teufel, James Allan, and Sadaoki Furui,
those for ACL 2005 by Hwee Tou Ng and Ke-
mal Oflazer, those for ACL 2002 by Eugene Char-
niak and Dekang Lin, and earlier ACL and EACL
formats, which were written by several people,
including John Chen, Henry S. Thompson and
Donald Walker. Additional elements were taken
from the formatting instructions of the Interna-
tional Joint Conference on Artificial Intelligence
and the Conference on Computer Vision and Pat-
tern Recognition.
References
Joshua Goodman. 2001a. A bit of progress in lan-
guage modeling. CoRR, cs.CL/0108005v1.
Joshua T. Goodman. 2001b. A bit of progress in
language modeling. Computer Speech & Lan-
guage, 15(4):403–434.
Rebecca Hwa. 1999a. Supervised grammar induc-
tion using training data with limited constituent
information. CoRR, cs.CL/9905001. Version 1.
Rebecca Hwa. 1999b. Supervised grammar induc-
tion using training data with limited constituent
information. In Proceedings of the 37th Annual
Meeting of the Association for Computational
Linguistics.
Daniel Jurafsky and James H. Martin. 2009.
Speech and Language Processing: An Intro-
duction to Natural Language Processing, Com-
putational Linguistics, and Speech Recognition,
second edition. Pearson Prentice Hall.

## Page 6

A
Author/Affiliation Options as set forth by MIT Press
Option 1. Author’s address is underneath each name, centered.
First Author
First Affiliation
First Address 1
First Address 2
first.email@example.com
Second Author
Second Affiliation
Second Address 1
Second Address 2
second.email@example.com
Third Author
Third Affiliation
Third Address 1
Third Address 2
third.email@example.com
Option 2. Author’s address is linked with superscript characters to its name, author names are grouped,
centered.
First Author⋄
Second Author†
Third Author‡
⋄First Affiliation
First Address 1
First Address 2
first.email@example.com
†Second Affiliation
Second Address 1
Second Address 2
second.email@example.com
‡Third Affiliation
Third Address 1
Third Address 2
third.email@example.com
