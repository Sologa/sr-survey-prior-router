# computational_linguistics (official_style_manual_pdf)

Source URL: https://submissions.cljournal.org/stylefiles/COLI_manual.pdf
Local raw file: `references/canonical_sources/raw/computational_linguistics/official_style_manual_pdf_coli_manual.pdf.pdf`

## Page 1

CLV2025 Class File Manual
How to Use CLV2025 LATEX Class File
Author A∗,1, Author B∗,1, Author C∗,1, Author D1, Author E2, Author F1,
Author G1, Author H2, Author I1, Author J3, Author K∗∗,2, Author L∗∗,1
1 Affiliation 1
corresponding@author_L.email
2 Affiliation 2
corresponding@author_K.email
3 Affiliation 3
This article describes how to use the “clv2025” class file, to produce typeset papers based on
Computational Linguistics typesetting specifications for submission to MIT. This document was
produced using the “clv2025” class file, derived from the earlier version “clv3” class file.
The content of this document is also based on its earlier version (by Odié N. Gementera from SPi
Publishing).
1. Introduction
This document applies to version 2025 of CL class file. It is assumed that the user has a
basic knowledge of LATEX typesetting commands.
2. Class File Options
There are several options available for switching the mode from a normal article to
manuscript style or to different layout styles. This is specified in the usual LATEX way by
declaring:
\documentclass[bookreview,manuscript]{clv2025}
bookreview: Sets the article layout for Book Review.
brief: Sets the article layout for Briefly Noted.
discussion: Sets the article layout for Squibs and Discussions.
pubrec: Sets the article layout for Publication Received.
shortpaper: Sets the article layout for Short Paper.
∗Equal contribution
∗∗Corresponding authors
Action editor: {action editor name}. Submission received: DD Month YYYY; revised version received: DD
Month YYYY; accepted for publication: DD Month YYYY.
© 2025 Association for Computational Linguistics

## Page 2

Computational Linguistics
Volume vv, Number nn
manuscript: Sets the baseline spacing to double space. This option can be used in
combination with other options.
By not specifying any option in the \documentclass command, the class file will
automatically default to the standard article layout.
3. Title Page
The title page is created using the standard LATEX command \maketitle. Before this
command is declared, the author must declare all the data which are to appear in the
title area.1
3.1 Volume, Number and Year
The commands \jvol{vv}\jnum{nn}\jyear{yyyy} are used in declaring the vol-
ume, number and year of the article. The first argument is for the volume, the second
argument is for the issue number. Volume and Issue number will appear on the even
page running head opposite the journal name. The third argument is for the Year which
will appear in the copyright line at the bottom of the title page.
3.2 Document Head
Document head is produced with the command \dochead{Document Head}. Doc
head will output differently, or may not appear at all, depending on the option used in
the documentclass.
3.3 Paper Title
The paper title is declared like: \title{Computer Linguistic Article} in the
usual LATEXmanner. Line breaks may be inserted with (\\) to equalize the length of the
title lines.
3.4 Authors
The name and related information for authors is declared with the \author{} com-
mand.
The \thanks{} command produces the "first footnotes." Such commands can be
used for indicating equal contributions or corresponding authors, etc. Please note that
LATEX\thanks cannot accommodate multiple paragraphs; authors will have to use a
separate \thanks for each paragraph.
The \affilblock{} command produces the author affiliations that appear to-
gether under the authors’ names. Within this block, the \affil{} command produces
individual affiliations, one for each affiliation. Please make sure the author names and
affiliations are aligned correctly by using commands such as $^{1}$ right after each
author name.
1 \maketitle is the command to execute all the title page information.
2

## Page 3

Author A et al.
CLV2025 Manual
3.5 Running Headers
The running heads are declared with the \runningtitle{Running Title} for the
journal name and \runningauthor{Author’s Surname} for author. These infor-
mation will appear on the odd pages. For bookreview option, odd page running
head is automatically set to "Book Reviews". Even page running head is default to
Computational Linguistics opposite volume and issue number.
3.6 Action Editor and Dates of Submission, Revision, and Acceptance
For regular papers, the name of the action editor and the dates of submission, revision,
and acceptance must appear in the footnote area of the title page, and they are declared
with the following command:
\pageonefooter{Action editor: \{action editor name\}.
Submission received: DD Month YYYY; revised version received:
DD Month YYYY; accepted for publication: DD Month YYYY.}.
However, please note that this command does not actually separate it into three lines;
instead, it should remain as a single line in your LATEX code.
For squib papers, there is no action editor and only the three dates need to be included.
4. Abstract
Abstract is the first part of a paper after \maketitle. Abstract text is placed within the
abstract environment:
\begin{abstract}
This is the abstract text . . .
\end{abstract}
5. Section Headings
Section
headings
are
declared
in
the
usual
LATEX
way
via
\section{},
\subsection{}, \subsubsection{}, and \paragraph{}. The first 3 levels
of section head will have Arabic numbering separated by period. The \paragraph{}
section will have the title head in Italics and at the same line with the first line of
succeeding paragraph.
6. Citations
Citations in parentheses are declared using the \cite{} command, and appear in the
text as follows: This technique is widely used (Woods 1970). The command \citep{}
(cite parenthetical) is a synonym of \cite{}.
Citations used in the sentence are declared using the \namecite{} commands,
and appear in the text as follows: Woods (1970) first described this technique. The
command \citet{} (cite textual) is a synonym of \namecite{}.
This style file is designed to be used with the BibTeX style file compling.bst.
Include the command \bibliographystyle{compling} in your source file.
Citation commands are based on the natbib package; for details on op-
tions and further variants of the commands, see the natbib documentation.
3

## Page 4

Computational Linguistics
Volume vv, Number nn
In particular, options exist to add extra text and page numbers. For example,
\cite[cf.][ch.\ 1]{winograd} yields: (cf. Winograd 1972, ch. 1).
The following examples illustrate how citations appear both in the text and in the
references section at the end of this document.
1.
Article in journal: Akmajian and Jackendoff (1970); Woods (1970).
2.
Book: Altenberg (1987); Winograd (1972).
3.
Article in edited collection/Chapter in book: Cutler (1983); Sgall (1970);
Jurafsky and Martin (2000).
4.
Technical report: Appelt (1982); Robinson (1964).
5.
Thesis or dissertation: Baart (1987); Spärck Jones (1964); Cahn (1989).
6.
Unpublished item: Ayers (1992).
7.
Conference proceedings: Benoit and Bailly (1989).
8.
Paper published in conference proceedings: Krahmer et al. (1999);
Copestake, Lascarides, and Flickinger (2001).
7. Definition with Head
Definition with head is declared by using the environment:
\begin{definition}
Definition text. . .
\end{definition}
This environment will generate the word “Definition 1” in bold on separate line.
The sequence number is generated for every definition environment. Definition data
will have no indention on the first line while succeeding lines will have hang indention.
8. Lists
The usual LATEX itemize, enumerate and definition list environments are used in
CLV2025 style.
To produce Numbered List use the environment:
\begin{enumerate}
\item First numbered list item
\item Second numbered list item
\item Third numbered list item
\end{enumerate}
To produce Bulleted List use the environment:
\begin{itemize}
\item First bulleted list item
\item Second bulleted list item
\item Third bulleted list item
\end{itemize}
4

## Page 5

Author A et al.
CLV2025 Manual
To produce Definition List use the environment:
\begin{deflist}
\item[First]
Definition list item. . .
\item[Second] Definition list item. . .
\item[Third]
Definition list item. . .
\end{deflist}
Additional list environment were also defined such as Unnumbered, Arabic and
Alpha lists.
Unnumbered List is the list where item labels are not generated. To produce Un-
numbered List use the environment:
\begin{unenumerate}
\item First list item
\item Second list item
\item Third list item
\end{unenumerate}
To produce Arabic List use the environment:
\begin{arabiclist}
\item First arabic list item
\item Second arabic list item
\item Third arabic list item
\end{arabiclist}
To produce Alpha List use the environment:
\begin{alphalist}
\item First alpha list item
\item Second alpha list item
\item Third alpha list item
\end{alphalist}
All the list environments mentioned above can be nested with each other.
8.1 Other List Types
8.1.1 Outline List or Example List.
\begin{exlist}
\item First outline list item. . .
\item Second outline list item. . .
\item Third outline list item. . .
\end{exlist}
8.1.2 Output Formula or Algorithm.
\begin{algorithm}
\item[Step 1] First item. . .
\item[Step 2] Second item. . .
\end{algorithm}
See sample on the COLI-template.pdf.
5

## Page 6

Computational Linguistics
Volume vv, Number nn
9. Word Formula or Displayed Text
Word formula and displayed text are text that should be displayed in a separate line
without indention. This are achieved by using the environment:
\begin{displaytext}
This is a sample of displayed text . . .
\end{displaytext}
10. Dialogue
Dialogue text are presentation of people’s conversation. These will be presented on a
separate line where each dialogue starts with the name of speaker, followed by colon.
Succeeding lines will be hang indented. To produce Dialogue use the environment:
\begin{dialogue}
Speaker 1: dialogue. . .
Speaker 2: dialogue. . .
\end{dialogue}
Please make sure to insert an empty line between dialogues.
11. Extracts
Extract text acts like quote, where left and right margins are indented. To produce
Extract use the environment:
\begin{extract}
This is an example of Extract text. . .
\end{extract}
See sample on the COLI-template-v2015.pdf.
12. Theorem-like Environments
There are several theorem-like environments defined in CLV2025 class file. Theorem-
like environments generate the name of the theorem as label, and counter number in
bold.
12.1 Example
To produce Example use the environment:
\begin{example}
This is Example text. . .
\end{example}
12.2 Lemma
To produce Lemma use the environment:
6

## Page 7

Author A et al.
CLV2025 Manual
\begin{lemma}
Lemma text. . .
\end{lemma}
This produces the following output:
Lemma 1
Lemma text.
A small vertical space separates the end of the lemma from the following text.
12.3 Theorem
To produce Theorem use the environment:
\begin{theorem}
Theorem text. . .
\end{theorem}
This produces the following output:
Theorem 1
Theorem text.
A small vertical space separates the end of the theorem from the following text.
12.4 Proof
The proof environment produces a square at the end of the text. To produce Proof use
the environment:
\begin{proof}
Proof text. . .
\end{proof}
This produces the following output:
Proof. Proof text.
A small vertical space separates the end of the lemma from the following text.
12.5 Unnumbered Theorem-like Environments
There are also unnumbered version of some of the theorem-like environments. These
are declared by using its asterisked version. Here are the three unnumbered version of
theorem-like environments:
\begin{theorem*}
Unnumbered theorem text. . .
\end{theorem*}
13. Appendix
Appendix is declared by issuing the command \appendix. This will set the necessary
labels to appendix’s rule (i.e. (A.1) for equation number).
7

## Page 8

Computational Linguistics
Volume vv, Number nn
Sections inside Appendix are declared using \appendixsection{}, which will
produce Appendix A: Section Title for first section.
Equation numbers are automatically set to (A.1), (A.2) and (A.3). Where the letters
follow the current level of Appendix section. So equations on Appendix B will have
equation numbers as follow: (B.1), (B.2) and (B.3).
14. Acknowledgments
Acknowledgments are produce by using the environment:
\begin{acknowledgments}
Acknowledgments text. . .
\end{acknowledgments}
15. Others
Other items, such as equations, figures, tables, and references, are produced using the
standard LATEX typesetting. Please refer to COLI-template.pdf for an example and COLI-
template.tex for its corresponding source.
References
Akmajian, Adrian and Ray Jackendoff. 1970.
Coreferentiality and stress. Linguistic
Inquiry, 1(1):124–126.
Altenberg, Bengt. 1987. Prosodic Patterns in
Spoken English: Studies in the Correlation
between Prosody and Grammar for
Text-to-Speech Conversion, volume 76 of
Lund Studies in English. Lund University
Press, Lund.
Appelt, Douglas E. 1982. Planning
natural-language utterances to satisfy
multiple goals. Technical Report 259, SRI.
Ayers, Gail M. 1992. Discourse functions of
pitch range in spontaneous and read
speech. Paper presented at the Linguistic
Society of America annual meeting.
Baart, J. L. G. 1987. Focus, Syntax, and Accent
Placement. Ph.D. thesis, University of
Leyden, Leyden.
Benoit, Christian and Gerard Bailly, editors.
1989. Proceedings of the Eurpoean Speech
Communication Association Workshop on
Speech Synthesis, Autrans, September.
European Speech Communication
Association. Institut de la Communication
Parlee, Grenoble.
Cahn, Janet E. 1989. Generating expression
in synthesized speech. Master’s thesis,
Massachusetts Institute of Technology,
May.
Copestake, Ann, Alex Lascarides, and Dan
Flickinger. 2001. An Algebra for Semantic
Construction in Constraint-Based
Grammars. In Proceedings of the 39th
Annual Conference of the Association for
Computational Linguistics (ACL-01), pages
140–147, Toulouse, France.
Cutler, Anne. 1983. Speakers’ conception of
the functions of prosody. In Anne Cutler
and D. Robert Ladd, editors, Prosody:
Models and Measurements. Springer-Verlag,
Berlin, pages 79–92.
Jurafsky, Daniel and James H. Martin. 2000.
Speech and Language Processing, chapter 1.
Prentice Hall.
Krahmer, Emiel, M. Swerts, Mariet Theune,
and M. Weegels. 1999. Error spotting in
human-machine interactions. In
Proceedings of EUROSPEECH-99, pages
1423–1426, Budapest.
Robinson, Jane J. 1964. Automatic parsing
and fact retrieval: A comment on
grammar, paraphrase, and meaning.
Memorandum RM-3892-PR, The RAND
Corporation, Santa Monica, CA.
Sgall, Petr. 1970. L’ordre des mots et la
semantique. In Ferenc Kiefer, editor,
Studies in Syntax and Semantics. D. Reidel,
New York, pages 231–240.
Spärck Jones, Karen. 1964. Synonymy and
Semantic Classification. D.Phil. dissertation,
Cambridge University, Cambridge,
England.
Winograd, Terry. 1972. Understanding Natural
Language. Academic Press, New York.
Woods, William A. 1970. Transition network
grammars for natural language analysis.
Communications of the ACM,
13(10):591–606.
8
