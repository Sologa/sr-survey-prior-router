# tacl_submission (official_transacl_submission_formatting_pdf)

Source URL: https://transacl.org/tacl-submission-templates/tacl2021v1-submission-formatting-instructions.pdf
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/tacl_submission/official_transacl_submission_formatting_pdf_tacl2021v1-submission-formatting-instructions.pdf.pdf`

## Page 1

1
000
001
002
003
004
005
006
007
008
009
010
011
012
013
014
015
016
017
018
019
020
021
022
023
024
025
026
027
028
029
030
031
032
033
034
035
036
037
038
039
040
041
042
043
044
045
046
047
048
049
050
051
052
053
054
055
056
057
058
059
060
061
062
063
064
065
066
067
068
069
070
071
072
073
074
075
076
077
078
079
080
081
082
083
084
085
086
087
088
089
090
091
092
093
094
095
096
097
098
099
Confidential TACL submission. DO NOT DISTRIBUTE.
Formatting Instructions for TACL Submissions
(Base files: tacl2021v1-template.tex & tacl2021v1.sty, dated Dec. 15, 2021)
Anonymous TACL submission
Abstract
This document contains the formatting re-
quirements for TACL submissions. These
formatting rules take effect for all submis-
sions received from September 2, 2018 on-
wards.
1
Courtesy warning: Common violations
of submission rules that have resulted
in desk rejects
1. Violation: wrong paper format.
As of the
September 2018 submission round and be-
yond, TACL requires A4 format.
This is a
change from the prior paper size.
2. Violation: main document text smaller than
11pt, or table or figure captions in a font
smaller than 10pt. See Table 1.
3. Violation: fewer than seven pages of content
or more than ten pages of content, including
any appendices. (Exceptions are made for re-
submissions where a TACL Action Editor ex-
plicitly granted a set number of extra pages to
address reviewer comments.) See Section 4.
4. Violation: Author-identifying information in
the document content or embedded in the file
itself.
• Advice: Make sure the submitted PDF
does not embed within it any author
info: check the document properties be-
fore submitting.
Useful tools include
Adobe Reader and pdfinfo.
• Advice: Check that no URLs (or cor-
responding websites) inadvertently dis-
close any author information.
If soft-
ware or data is to be distributed, mention
so in anonymized fashion.
• Advice: Make sure that author names
have been omitted from the author
block. (It’s OK to include some sort of
anonymous placeholder.)
• Advice: Do not include acknowledg-
ments in a submission.
• Advice: While citation of one’s own
relevant prior work is as encouraged as
the citation of any other relevant prior
work, self-citations should be made in
the third, not first, person. No citations
should be attributed to “anonymous” or
the like. See Section 10.2.
2
General instructions
Submissions that do not comply with this docu-
ment’s instructions risk rejection without review.
Submissions should consist of a Portable Docu-
ment Format (PDF) file formatted for A4 paper.1
All necessary fonts should be included in the file.
3
LATEX files
LATEX files compliant with these instructions are
available at the Author Guidelines section of the
TACL website, https://www.transacl.org.2 Use of
the TACL LATEX files is highly recommended: MIT
Press requires authors to supply LATEX source files
as part of the publication process; and use of the
recommended LATEX files makes conversion to the
required camera-ready format simple.
3.1
Workarounds for problems with the
hyperref package
The provided files use the hyperref package by de-
fault. The TACL files employs the hyperref pack-
age to make clickable links for URLs and other
1Prior to the September 2018 submission round, a differ-
ent paper size was used.
2Last accessed Dec. 15, 2021.

## Page 2

2
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
Confidential TACL submission. DO NOT DISTRIBUTE.
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
To disable it,
add nohyperref in the
square brackets to pass that option to the
TACL
package.
For
example,
change
\usepackage[]{tacl2021v1}
to
\usepackage[nohyperref]{tacl2021v1}.
4
Length limits
Submissions may consist of seven to ten (7-10) A4
format (not letter) pages of content.
The page limit includes any appendices. How-
ever, references do not count toward the page
limit.
Exception: Revisions of (b) or (c) submissions
may have been allowed additional pages of con-
tent by the prior Action Editor, as specified in their
decision letter.
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
3Indeed, for some versions of acl_natbib.sty, DOIs and
URLs are not printed out or included in the bibliography in
any form if the hyperref package is not used.
4If the problematic link is part of a reference in the
bibliography and you do not wish to directly edit the
corresponding .bbl file, a heavy-handed approach is to add
the line \interlinepenalty=10000 just after the line
\sloppy\clubpenalty4000\widowpenalty4000
in the “\def\thebibliography” portion of the file
tacl2021v1.sty. This penalty means that LaTex will not allow
individual bibliography items to cross a page break.
5Should Times Roman be unavailable to you, use Com-
puter Modern Roman (LATEX2e’s default). Note that the latter
is about 10% less dense than Adobe’s Times Roman font.
Type of Text
Size
Style
paper title
15 pt
bold
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
6
Page Layout
The margin dimensions for a page in A4 format
(21 cm × 29.7 cm) are given in Table 2. Start the
content of all pages directly under the top margin.
(The confidentiality header (§6.1) for submissions
is an exception.)
Left and right margins: 2.5 cm
Top margin: 2.5 cm
Bottom margin: 2.5 cm
Column width: 7.7 cm
Column height: 24.7 cm
Gap between columns: 0.6 cm
Table 2: Margin requirements
Submissions must be in two-column format.
Allowed exceptions to the two-column format are
the title, which must be centered at the top of the
first page; the confidentiality header (see §6.1) on
submissions; and any full-width figures or tables.
Should the pages be numbered? Yes, for sub-
missions (to facilitate review); but no, for camera-
readies (page numbers will be added at publication
time).
Submissions should be single-spaced.
Indent by about 0.4cm when starting a new
paragraph that is not the first in a section or sub-
section.
6.1
The confidentiality header and
line-number ruler
Each page of the submission should have the
header “Confidential TACL submission. DO NOT
DISTRIBUTE.” centered across both columns in
the top margin.
Submissions must include line numbers in the
left and right margins, as demonstrated in the
TACL submission-formatting instructions pdf file,
because the line numbering allows reviewers to be

## Page 3

3
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
Confidential TACL submission. DO NOT DISTRIBUTE.
very specific in their comments.6 Note that the
numbers on the ruler need not line up exactly with
the text lines of the paper. (Indeed, the line num-
bers generated by the recommended LATEX files
typically do not correspond exactly to the text
lines.)
The presence or absence of the ruler or header
should not change the appearance of any other
content on the page.
7
The First Page
Center the title, which should be placed 2.5cm
from the top of the page, across both columns of
the first page. Long titles should be typed on two
lines without a blank line intervening. Do not in-
clude the paper ID number assigned during the
submission process.
Although submissions should not include any
author information, maintain space for names and
affiliations/addresses so that they will fit in the fi-
nal (camera-ready) version.
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
6Authors using Word to prepare their submissions can
create the marginal line numbers by inserting text boxes con-
taining the line numbers.
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
Self-citations
Citing one’s own relevant prior work should
be done,
but use the third person instead
of the first person,
to preserve anonymity:
Correct: Zhang (2000) showed ...
Correct: It has been shown (Zhang, 2000)...
Incorrect: We (Zhang, 2000) showed ...
Incorrect: We (Anonymous, 2000) showed ...
10.3
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
7If using BibTex, apply curly braces within the title field
to preserve intended capitalization.
8The supplied LATEX files will automatically add hyper-
links to the DOI when BibTeX or BibLateX are invoked if
the hyperref package is used and the doi field is employed
in the corresponding bib entries. The DOI itself will not be

## Page 4

4
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
Confidential TACL submission. DO NOT DISTRIBUTE.
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
• Include the version number when citing
arXiv preprints, even if only one version ex-
ists at the time of writing. For example,9 note
the “v1” in the following.
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
Contributors to this document
This document was adapted by Lillian Lee and
Kristina Toutanova from the instructions and files
for ACL 2018, by Shay Cohen, Kevin Gimpel, and
Wei Lu. This document was updated by Cindy
separately printed out in that case.
9Bibtex entries for Goodman (2001a) and Hwa (1999a)
corresponding to the depicted output can be found in the sup-
plied sample file tacl.bib. We also cite the peer-reviewed
versions (Goodman, 2001b; Hwa, 1999b), as required.
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

## Page 5

5
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
Confidential TACL submission. DO NOT DISTRIBUTE.
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
