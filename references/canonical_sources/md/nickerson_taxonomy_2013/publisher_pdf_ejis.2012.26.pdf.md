# A Method for Taxonomy Development and its Application in Information Systems (publisher_pdf)

Source URL: https://link.springer.com/content/pdf/10.1057/ejis.2012.26.pdf
Local raw file: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/raw/nickerson_taxonomy_2013/publisher_pdf_ejis.2012.26.pdf.pdf`

## Page 1

A method for taxonomy development and
its application in information systems
Robert C. Nickerson1,
Upkar Varshney2 and
Jan Muntermann3
1Department of Information Systems, College
of Business, San Francisco State University,
San Francisco, California, USA; 2Department
of Computer Information Systems, Robinson
College of Business, Georgia State University,
Atlanta, Georgia; 3Department of Information
Systems and Department of Finance, Accounting
and Taxes, University of Go¨ttingen, Go¨ttingen,
Germany
Correspondence: R.C. Nickerson,
Department of Information Systems,
College of Business, San Francisco State
University, 1600 Holloway Avenue,
San Francisco, California 94132, U.S.A.
Tel: þ 1-415-338-2138;
Fax: þ 1-415-405-0364;
E-mail: RNick@sfsu.edu
Received: 24 November 2010
Revised: 15 April 2012
Accepted: 17 April 2012
Abstract
A fundamental problem in many disciplines is the classification of objects in
a domain of interest into a taxonomy. Developing a taxonomy, however, is
a complex process that has not been adequately addressed in the information
systems (IS) literature. The purpose of this paper is to present a method for
taxonomy development that can be used in IS. First, this paper demonstrates
through a comprehensive literature survey that taxonomy development in IS
has largely been ad hoc. Then the paper defines the problem of taxonomy
development. Next, the paper presents a method for taxonomy development
that is based on taxonomy development literature in other disciplines and
shows that the method has certain desirable qualities. Finally, the paper
demonstrates the efficacy of the method by developing a taxonomy in a
domain in IS.
European Journal of Information Systems (2013) 22, 336–359.
doi:10.1057/ejis.2012.26; published online 19 June 2012
Keywords: taxonomy; typology; classification; taxonomy development; research meth-
odologies
Introduction
A fundamental problem in many disciplines is the classification of objects
of interest into taxonomies. Biology has studied this problem extensively
and developed a number of classification schemes that order the
complexity of the living world and provide a foundation for biological
research. Similar schemes are also found in many social science fields.
Taxonomies play an important role in research and management because
the classification of objects helps researchers and practitioners understand
and analyze complex domains. This universal character of taxonomies is
also highlighted by Miller & Roth (1994, p. 286) who note that ‘taxonomies
y are useful in discussion, research and pedagogy’.
The role of taxonomies is also well recognized in the information systems
(IS) research literature. Glass & Vessey (1995) note that taxonomies provide
a structure and an organization to the knowledge of a field, thus enabling
researchers to study the relationships among concepts and, therefore, to
hypothesize about these relationships. McKnight & Chervany (2001) argue
that taxonomies can order otherwise disorderly concepts and allow
researchers to postulate on the relationships among the concepts. Williams
et al (2008) illustrate the use of taxonomies in understanding the science
behind design principles of observed artifacts. Fiedler et al (1996, pp. 11–12)
state that classification (i.e., taxonomy) has been important in research
‘since Aristotelian applications over 2000 years ago’. Sabherwal & King
(1995, p. 180) present a further argument by pointing out that ‘taxonomies
also help us understand divergence in previous research findings’.
European Journal of Information Systems (2013) 22, 336–359
& 2013 Operational Research Society Ltd. All rights reserved 0960-085X/13
www.palgrave-journals.com/ejis/

## Page 2

From a philosophical foundations perspective, taxono-
mies are forms of conceptual knowledge in the epi-
stemology of design science (Iivari, 2007), which also
includes descriptive knowledge and prescriptive know-
ledge. As Iivari (2007, p. 46) explains ‘The research goal
at the conceptual level is essentialist: concepts and
conceptual frameworks at this level aim at identifying
essences in the research territory and their relationships’.
Conceptual knowledge, including taxonomies, does not
have a truth value but is relevant input for the deve-
lopment of theories representing forms of descriptive
knowledge, which have a truth value (Iivari, 2007).
Doty & Glick (1994) also argue that the classification of
objects (i.e., taxonomy) contribute to theory building.
This point is also stressed by Bapna et al (2004, p. 23),
who state that ‘a robust taxonomy can then be used to
perform ex post theory building’.
Taxonomy is a form of classification, and, as discussed
later, the terms, along with typology and framework,
are sometimes used interchangeably. Wand et al (1995,
p.
291)
note
that
classification
is
‘a
fundamental
mechanism for organizing knowledge’. The systematic
organization of knowledge is a long running concern in
IS
(Hirschheim
et
al,
1995).
Ontologies
have
been
proposed as one way of dealing with this concern and
have found their way into IS (Guarino, 1998). Ontologies,
defined by Gruber (1993) as explicit specifications of
conceptualizations, can include a number of artifacts
besides formal ontologies including thesauri, controlled
vocabularies, folksonomies, and taxonomies (Gruninger
et al, 2008). Often, however, these other artifacts –
including taxonomies – are viewed as distinct from
ontologies (Dogac et al, 2002), although Wand & Weber
(2004) note that theories of ontology sometimes function
like taxonomies. A taxonomy may be a step toward a
future ontology, however, just as the periodic table,
which can be viewed as a taxonomy of elements (Grove,
2003), was a step toward various ontologies in chemistry
(Pinto & Martins, 2004). Although we focus on taxonomy
development in this paper, ontology development is
worthy of study in future research.
As we will show later in this paper, IS researchers have
proposed a number of taxonomies over the years. In many
cases, however, the development of these taxonomies has
followed a largely ad hoc approach. Although the process
of developing a taxonomy has been studied in a number
of disciplines (e.g., Eldredge & Cracraft, 1980, and Sokal &
Sneath, 1963, in biology; Bailey, 1994, in the social
sciences), little has been written about this process in the
IS field. Glass & Vessey (1995) note the lack of a taxonomy
development methodology in their review of application-
focused taxonomies. A well-conceived method for deve-
loping taxonomies would serve as a basis for developing
new taxonomies in IS that could bring order to complex
areas and potentially lead to new research directions. The
general purpose of this paper is to present such a method.
Before creating a taxonomy development method, we
need to examine how taxonomies are developed by other
researchers in IS. This paper presents a survey of IS
literature that identifies common themes related to taxo-
nomies and taxonomy development. On the basis of this
literature survey, we define the problem of taxonomy
development. This problem definition serves as a guide
for the creation of the taxonomy development method
described in this paper.
After
creating
a
taxonomy
development
method
we need to demonstrate its efficacy by applying it to spe-
cific domains. This paper uses the method to develop
a taxonomy in one IS domain, that of mobile applica-
tions. We have chosen this domain because of its
increasing importance and complexity with many new
applications appearing regularly. Users, researchers, and
developers need to be able to know where a new
application fits with existing ones in this domain in
order to determine if it is something entirely new and
unique, a significant variation of an existing application,
or just a retread of what we already have. A taxo-
nomy provides a basis for making this determination
and could point out voids where new applications might
be developed.
Our research approach to creating a taxonomy deve-
lopment method is based on the design science research
paradigm, which aims to address new knowledge about
artificial (i.e., manmade) objects that are designed to
meet certain goals and provide utility to their users
(Simon, 1969). March & Smith (1995) present four kinds
of contributions (artifacts) – constructs, models, methods,
and instantiations – and two processes (research activi-
ties) – artifact building and artifact evaluation – that
characterize design science research in IS. In this paper,
we present a method that is intended to support design
researchers during their research activities when deve-
loping a taxonomy for a specific domain. This method
is an artifact that serves as a basis for future design
science research, the purpose of which is to develop
new taxonomies. These new taxonomies are artifacts
(models) in themselves. In terms of research processes, we
first build an artifact (method) for developing taxo-
nomies. Then we evaluate the artifact we have built
by using it to develop (i.e., build) a taxonomy that des-
cribes and classifies existing or future objects in a specific
domain. Since the result of this second step is an artifact
(taxonomy), it is subject to evaluation. We evaluate the
taxonomy by assessing its efficacy in classifying objects of
interest in the specific domain.
This paper is organized as follows. First, we define
certain fundamental terms used in this paper. Then we
discuss taxonomy development in other disciplines.
Next, we present our literature survey and our analysis
of the papers surveyed. Then we present our problem
statement for creating a taxonomy development method.
Following these topics, we present our method for deve-
loping taxonomies and justify it based on the foundation
we have laid. Next, we demonstrate the use of our
taxonomy development method by developing a taxo-
nomy of mobile applications. We conclude the paper
A method for taxonomy development
Robert C. Nickerson et al
337
European Journal of Information Systems

## Page 3

with an extended discussion, summary of our results, and
suggestions for future research.
Classifications, frameworks, typologies, and
taxonomies
We are concerned with systems for grouping objects of
interest in a domain based on common characteristics.
We find that different terms are used for such systems,
and that these terms are often confused. Before pro-
ceeding we need to clarify these terms and explain how
we use them in this paper. We note that this is not an
easy task, or, as Sokal & Sneath (1963, p. 2) say ‘The ade-
quate definition of taxonomic terms would almost
require a book by itself’.
The term classification is used to refer to both the system
or
process
of
organizing
objects
of
interest
and
the organization of the objects according to a system.
Bowker & Star (1999, p. 10) use the term classification for
‘a spatial, temporal, or spatio-temporal segmentation
of the world’ and the term classification system for ‘a set
of boxes (metaphorical or literal) into which things can
be put to then do some kind of work’. Bailey (1994, p. 1)
uses the term classification as the process of ‘ordering
entities into groups or classes on the basis of similarity’.
He says that classification can be unidimensional or
multidimensional, and that it can be done conceptually
or empirically. Doty & Glick (1994), on the other hand,
use the term classification scheme for a system that
groups objects by applying specific ‘decision rules’. In this
paper, we use the term classification system for the
abstract groupings or categories into which we can put
objects and the term classification for the concrete result
of putting objects into groupings or categories.
Framework is another general term used for organizing
objects. In their paper on framework and review articles,
Schwarz et al (2007, p. 41) implicitly define a framework
in the context of framework articles as a ‘set of assump-
tions, concepts, values, and practices that constitutes
a way of understanding the research within a body of
knowledge’. Their definition is closest to that of a classi-
fication system discussed above and could be used
synonymously with it in some instances. They also pro-
vide 10 purposes of a framework article and 17 qualities
of a framework within their context, many of which over-
lap our formal definition of taxonomy and our necessary
conditions for a taxonomy to be useful that we discuss
later in this paper. Interestingly, they also provide what
we would call a taxonomy for framework and review
articles with six dimensions.
The term typology is usually restricted to a system of
conceptually derived groupings. Both Bailey (1994) and
Doty & Glick (1994) use the term this way. Bailey also
notes that typologies are usually multidimensional and
distinguishes them from simple unidimensional classi-
fication systems, implying that typologies are usually
more complex than classification systems.
The term taxonomy is perhaps the most confused.
As with classification, taxonomy is sometimes used for
the system or process and sometimes used for the result
of applying the system (Bailey, 1994). We could refer to
the former as a taxonomic system and the later as
a taxonomy, but we will follow the common practice of
using the term taxonomy for both and allow the context
to make it clear what we are referring to. In some
literature, taxonomy is restricted to empirically derived
groupings, often found through cluster analysis or some
other statistical technique. This form of taxonomy is
sometimes called numerical taxonomy (Sokal & Sneath,
1963). Doty & Glick (1994) equate taxonomy with
classification scheme, although they note that classifi-
cation scheme, taxonomy, and typology are often used
interchangeably.
Gregor
(2006,
p.
623)
echoes
this
thought, stating that ‘the term typology is used more or
less synonymously for taxonomy and classifications’.
Bailey (1994) distinguishes taxonomies (classification
systems derived empirically) from typologies (classifi-
cation systems derived conceptually). As we will see,
however, Bailey presents a methodology for developing
taxonomies/typologies that is a combination of concep-
tual and empirical approaches.
Much literature, however, uses taxonomy for systems
of groupings that are derived conceptually or empirically.
We
make
this
observation
in
the
literature
survey
discussed later in this paper. We also find in our literature
survey that taxonomy is by far the most common term
and thus we choose to use it throughout this paper
whether we are referring to a conceptually or empirically
derived grouping. We note that we could use any of
the terms discussed here – classification, framework,
typology, or taxonomy – for the object of study in this
paper, and we recognize that in some situations taxo-
nomy may not be the most precise term, but we opt for
common recognition over precision in this paper and use
taxonomy exclusively.
Taxonomy development in other disciplines
Developing a taxonomy is a complex process. Biology,
with its well-known taxonomy of living organisms,
provides some guidance. The traditional Linnaean taxo-
nomy, commonly found in biology textbooks, classifies
organisms based on a predefined hierarchy of categories
from kingdom to species. Determining where a new
organism falls in the taxonomy involves identifying into
which classification the organism fits at each level of the
hierarchy. However, biological taxonomy development is
not limited to the traditional approach. Taxonomists also
use phenetics and cladistics. Phenetics, sometimes called
numerical
taxonomy,
involves
classifying
organisms
solely on the basis of their similarity. The researcher
identifies different characteristics of organisms and then
uses statistical techniques to cluster the organisms into
similar groups based on these characteristics (Sokal &
Sneath, 1963). In contrast, cladistics does not look at
common characteristics but rather examines the evo-
lutionary relationships among organisms (Eldredge &
Cracraft, 1980). The researcher investigates the evolution
A method for taxonomy development
Robert C. Nickerson et al
338
European Journal of Information Systems

## Page 4

of organisms from others and then groups organisms
based on their evolutionary heritage. Two organisms may
be closely related in a cladistic taxonomy because they
have a common ancestor even though they do not share
certain characteristics, thus putting them in different
groups in a phenetic analysis.
Taxonomy development in the social sciences has
also been well studied. Bailey (1994) provides a thorough
survey of the subject. As noted previously, Bailey distin-
guishes between a typology and a taxonomy, saying that
the former is derived conceptually or deductively and
the latter is derived empirically or inductively. In the
conceptual typology approach, the researcher proposes
a typology of categories or types based on a theoretical
ideal or model. In the process, the researcher could
define an ideal type, which Bailey (citing Weber, 1949)
explains is the ‘extreme’ or ‘nirvana’ of types. The ideal
type is used to examine empirical cases in terms of how
much they deviate from the ideal. Alternatively, in the
empirical approach the researcher proposes a taxonomy
based on a constructed type, which, as Bailey (citing
McKinney, 1966) explains, is not the ideal but based
on reference to empirical cases. The constructed type is
used to examine ‘exceptions’ to the type. Bailey compares
the ideal type with the highest value in a set of data
(assuming highest is best) and the constructed type to the
mean of the data (Bailey, 1994, p. 23).
In Bailey’s conceptual approach, the researcher deve-
lops a typology starting with a conceptual or theoretical
foundation and then derives the typological structure
through deduction. The researcher may conceive of a
single type and then add dimensions until a satisfactorily
complete typology is reached, a process called substruc-
tion (Bailey, 1994, p. 24). Alternatively, the researcher
could conceptualize an extensive typology and then
eliminate certain dimension in a process called reduction
(Bailey, 1994, p. 24) until a sufficiently parsimonious
typology is reached.
The conceptual approach is not based on empirical
data, although such data could be brought in toward the
end of the process for verification purposes. The empiri-
cal approach, on the other hand, starts with data and
derives the classification from this data using cluster
analysis or other statistical methods (Bailey, 1994, p. 34).
The goal is to find similarities among the data and to
classify similar objects into the same category. Each cate-
gory in the resulting taxonomy is called a taxon (plural
taxa). Using the concepts from biology, this approach is
phenetic.
Bailey (1984) describes the approaches just examined
as different levels – conceptual and empirical – of a
two-level model. Although researchers can approach
classification through either level, he suggests that a com-
mon and often more useful approach is to use a three-
level model that includes conceptual, empirical, and
indicator or operational levels. In this method the resea-
rcher has two choices. One is to start with the con-
ceptual approach and then to examine empirical cases
(conceptual to empirical) to see how they fit with the
conceptualization. The other choice is to start with
empirical data clusters and then to deductively con-
ceptualize the nature of each cluster (empirical to
conceptual). We note that in this three-level model
Bailey combines typology development through con-
ceptualization with taxonomy development through
empirical data analysis to arrive at the final classification.
Survey of taxonomy development literature
In order to examine taxonomy development in IS, we
conducted a literature survey of papers that have a focus
on the development of taxonomies. As a basis for the
literature survey, we used the AIS Journal Rankings page
available from the AIS website (http://ais.affiniscape
.com/displaycommon.cfm?an ¼ 1&subarticlenbr ¼ 432).
From this ranking, we surveyed the top 30 journals and
searched for papers that have the words taxonomy/ies
or typology/ies in their title and that were published
up to the year 2009. Further, we included papers
published in ICIS, AMCIS, ECIS, PACIS, and HICSS pro-
ceedings. We identified 73 relevant papers that propose
new taxonomies.
The AIS Journal Rankings focus on IS papers but
also includes journals from computer science (CS) and
non-information
systems
business
(Bus)
disciplines.
We included papers in these closely related research
fields to see how they compare. All papers surveyed
are listed in the Appendix of this paper. We classified
each paper by its principal domain: IS, CS, and Bus. We
recognize that the line between IS and CS is sometimes
not clear. For borderline cases, we classified a paper as
IS if it emphasized the organizational/managerial aspects
of the topic and as CS if it emphasized the technical
aspects. Papers in e-commerce (including mobile com-
merce) were classified as IS. Bus papers include papers
in marketing, operations, management, and other areas
of business. The publishing journal also provided an
indication of how to classify a paper. For example, ACM
journals generally publish papers in CS and journals such
as EJIS, MISQ, and ISR generally focus on IS research. We
identified 41 IS papers, 20 CS papers, and 12 papers in Bus
fields.
For each paper we noted the type of taxonomy it
developed and the approach or method that the authors
used for developing its taxonomy. We classified the
approach into one of the following categories:
 Inductive
 Deductive
 Intuitive
The inductive approach involves observing empirical
cases, which are then analyzed to determine dimensions
and characteristics in the taxonomy. The analysis may
be done using statistical techniques such as cluster
analysis or may use less rigorous techniques; we noted
this in our survey. This methodology is called phenetics
A method for taxonomy development
Robert C. Nickerson et al
339
European Journal of Information Systems

## Page 5

or numerical taxonomy in biology. Bailey (1994) calls this
the empirical approach in sociology.
The deductive approach derives a taxonomy not from
empirical cases but instead from theory or conceptuali-
zation. It identifies dimensions and characteristics in the
taxonomy by a logical process derived from a sound
conceptual or theoretical foundation. Cladistics in bio-
logy is similar to this approach. In sociology, Bailey
(1994) identifies this as the conceptual approach. This
approach may be followed by an analysis of empirical
cases to evaluate and perhaps modify the taxonomy.
The intuitive approach is essentially ad hoc. The
researcher uses his or her understanding of the objects
to be classified to propose a taxonomy based on the
researcher’s perceptions of what makes sense. There is no
explicit method in this approach.
Several other approaches were found that did not fall
into these categories including morphological analysis
and the use of existing taxonomies.
Table 1 shows the distribution of approaches used in
the IS, CS, and Bus papers that we surveyed.
In a previous paper (Nickerson et al, 2010), we provide
a detailed analysis of 65 papers. For the current research
we excluded some papers that did not meet our selection
criteria and identified additional papers that meet the
criteria. The result is the 73 papers surveyed in this
research. The ease with which we found a large number of
papers that use the term taxonomy or typology in their
titles indicates to us that there is interest in classification
schemes in IS and the other fields examined.
Of the papers we found, 56 use the term taxonomy
and 17 use the term typology. Overwhelmingly, the most
common term used is taxonomy. However, there appears
to be a great deal of confusion about what a taxonomy is.
Some papers seem to use the word taxonomy to show
that they are aware of the literature related to their pro-
blem area. They classify the literature into two or three
simple categories, which may not completely define their
domain.
Other
papers
present
lists
as
taxonomies,
including lists of functions someone has to perform.
Published taxonomies range from very simple to
complex. Some papers present simple N  N (N ¼ 2, 3, 4)
classifications. Most papers present taxonomies with four
or fewer dimensions, but a few papers give taxonomies
with more than 10 dimensions. There is no agreement on
what represents an appropriate number of dimensions.
Many papers provide little information about the
method the authors used to develop their taxonomies,
so we could not identify the approach used in these
papers. In fact, we classified over 40% (30) of the
surveyed papers as not identifying the method used. In
some cases, we were able to infer the method from other
comments in the paper. When we could not, we inter-
preted these papers as using a purely intuitive approach
based on the author’s perception of what is a good
classification for its intended purpose. We recognize that
our interpretation may be incorrect in some instances.
Several other papers were classified as using an intuitive
approach. In total, we classified nearly one-third (24) of
the surveyed papers as using an intuitive approach.
Many papers do not base their taxonomy on a con-
ceptual, theoretical, or empirical foundation. Although
authors review the literature in their problem area, their
taxonomy is often not based on their literature review
but instead is ad hoc. We classified these as using an
intuitive approach.
Of the papers that use an inductive approach (27),
about half (14) use statistical analysis to identify clusters
appropriate for their taxonomy. The other half (13) use
informal techniques to examine their empirical cases.
Papers that use a deductive approach (19) were hard to
identify. Some of the papers that we identified as using an
intuitive approach may, in fact, use a deductive approach.
We could not find any relationship between the deve-
lopment method used and the term – taxonomy or typo-
logy – used for the final grouping. Although typologies
are usually identified with a deductive approach and
taxonomies with an inductive approach, this relationship
was not evident in the papers we surveyed.
Papers in business tend to be more formal in their app-
roach whereas papers in CS and IS tend to be less formal.
Papers in the IS domain use the most diverse taxonomy
development approaches.
Few papers cite the taxonomy development literature
from other disciplines that we have identified.
A general conclusion from this survey is that many
researchers in IS find taxonomies useful, and that a
taxonomy development method that researchers can use
in place of ad hoc methods may be beneficial.
Problem statement for taxonomy development
In this section, we state the research problem that we are
exploring, that of defining a method for taxonomy
development that can be used in the IS field.
To start we define what we mean by a taxonomy. A
taxonomy T is a set of it n dimensions Di (i ¼ 1, y, n) each
consisting of ki (kiX2) mutually exclusive and collectively
exhaustive characteristics Cij (j ¼ 1, y, ki) such that each
object under consideration has one and only one Cij for
each Di. Stated another way,
T ¼ fDi; i ¼ 1; . . . ; njDi ¼ fCij; j ¼ 1; . . . ; ki; kiX2gg
Table 1
Taxonomy development in different domains
Taxonomy development approach
Principal
domain
Inductive
(statistical
analysis)
Inductive
(informal
analysis)
Deductive
(may be followed
by empirical
verification)
Intuitive
Other
IS
7
10
9
13
2
CS
1
3
6
10
0
Bus
6
0
4
1
1
Total
14
13
19
24
3
A method for taxonomy development
Robert C. Nickerson et al
340
European Journal of Information Systems

## Page 6

The mutual exclusive restriction means that no object
can have two different characteristics in a dimension. The
collectively exhaustive restriction means that each object
must have one of the characteristics in a dimension.
Together these conditions mean that each object has
exactly one of the characteristics in each dimension.
We find a number of other terms used for dimension
and characteristic. Sometimes dimension is called vari-
able and the characteristics of a dimension are the possi-
ble values (domain) of the variable. This terminology
is
common
in
the
cluster
analysis
literature
(e.g.,
Anderberg, 1973; Aldenderfer & Blashfield, 1984). Sokal
& Sneath (1963), in their foundational book on numeri-
cal taxonomy, use the terms taxonomic character and
character state, which are standard terms in biology.
Doty & Glick (1994) use attribute and value, respectively.
Bailey (1994) uses dimension for typologies and vari-
able for taxonomies. In our survey of the literature
we found a variety of terms including category and
capability, and characteristic and dimension with their
meanings reversed. We choose to use dimension and cha-
racteristic as above because they are at least as common
as others, they can apply to all forms of classification, and
they are descriptive.
We want to develop useful taxonomies, but not nece-
ssarily ‘best’ or ‘correct’ ones, as these cannot be defined
and, in fact, may be moving targets that could change
over time. In the design science literature, this problem of
not being able to find an optimal solution is described as
design as a search process. As stated by Hevner et al (2004,
p. 88), ‘The search for the best, or optimal, design is
often intractable for realistic information systems pro-
blems’. Instead, the search process attempts to discover
effective – or useful – solutions. The taxonomy develop-
ment literature gives us little help with metrics for
evaluating taxonomies regarding effectiveness or useful-
ness. Indeed, Bailey (1994, p. 2) makes this clear when he
repeatedly asks which of his example classifications is
‘best’ without giving guidance for finding the answer
other than saying that ‘a classification is no better
than the dimensions or variables on which it is based’.
Later, he lists ‘weaknesses’ of typologies including lack
of mutual exclusivity and collective exhaustivity; lack of
parsimony; lack of changeability (i.e., they are static);
based on criteria that are arbitrary or ad hoc; and
descriptive rather than explanatory (Bailey, 1994, p. 34).
We note that we found these weaknesses in some of the
proposed taxonomies surveyed previously. Bowker & Star
(1999) also note the importance of mutual exclusivity in
a classification system. In addition, they include com-
pleteness, in the sense of covering all objects in a domain,
as an important property of a classification system.
Parsons & Wand (2008) propose that the ability to draw
inferences is a critical condition for a useful classification,
although not specifically a taxonomy. The authors define
an inference as ‘the ability to infer some properties of an
instance by virtue of identifying it as a member of a class,
without having to directly observe these properties’
(Parsons & Wand, 2008, p. 843). While this condition
may be desirable for some uses of a taxonomy, it is not
universally required. Many useful taxonomies have been
developed that do not meet this condition, including, we
contend, the Linnaean taxonomy of biology.
Without detailed guidance from the literature we are
left on our own to define a useful taxonomy. We propose
that a useful taxonomy has the following qualitative
attributes:
 It is concise: A useful taxonomy should be parsimonious,
for, as Bailey (1994) notes, lack of parsimony is a
weakness. A taxonomy should contain a limited number
of dimensions and a limited number of characteristics in
each dimension, because an extensive classification
scheme with many dimensions and many characteristics
may exceed the cognitive load of the researcher and thus
be difficult to comprehend and apply. We could state
this attribute formally as a function of the number of
dimensions and the number of characteristics that must
have values less than maximums defined by factors
including cognitive capacity in decision making. We
leave this analysis for future research.
 It is robust: A useful taxonomy should contain enough
dimensions and characteristics to clearly differentiate
the objects of interest. A taxonomy with few dimen-
sions and characteristics may not be able to adequately
differentiate among objects. For example, a taxonomy
with only one dimension and two characteristics
within that dimension would not usually be useful.
Bailey (1994, p. 1) makes this clear when he says that
the goal is to ‘make groups that are as distinct (non-
overlapping) as possible, with all members within a
group being as alike as possible’. This attribute can
conflict with the conciseness attribute. As with the
conciseness attribute, we could state the robustness
requirement as a function of the number of dimen-
sions and the number of characteristics that must have
values greater than minimums needed to characterize
the objects of interest. Again, we leave this analysis for
future research.
 It is comprehensive: This attribute can be interpreted
two ways. One interpretation is that a useful taxonomy
can classify all known objects within the domain under
considerations. This corresponds to Bowker & Star’s
(1999) requirement of completeness. Taxonomies that
are developed empirically should display this attribute.
The second interpretation is that a useful taxonomy
includes all dimensions of objects of interest. Doty &
Glick (1994, p. 294) imply this when, discussing ideal
types in typologies, they say that ‘typologies must
provide complete descriptions of each ideal type using
the same set of dimensions’. Taxonomies that are
developed conceptually should display this attribute.
 It is extendible: A useful taxonomy should allow for
inclusion of additional dimensions and new character-
istics within a dimension when new types of objects
appear. A taxonomy that is not extendible may soon
A method for taxonomy development
Robert C. Nickerson et al
341
European Journal of Information Systems

## Page 7

become obsolete. Put another way, it is dynamic, not
static. Bailey (1994) points out that lack of change-
ability is a weakness.
 It is explanatory: A useful taxonomy contains dimen-
sions and characteristics that do not describe every
possible detail of the objects but, rather, provide useful
explanations of the nature of the objects under study
or of future objects to help us understand the objects.
A taxonomy that simply describes objects may be of
interest initially but will have little value in under-
standing the objects being classified. Bailey (1994)
notes that typologies that are descriptive rather than
explanatory are weak. This attribute allows a taxonomy
to be used to identify where an object is found in
the taxonomy or to identify the characteristics of an
object found in the taxonomy. That is, if someone
knows the characteristics of an object, he/she will find
the object in an identifiable spot in the taxonomy, or if
someone finds an object in a specific spot in the
taxonomy, he/she will be able to identify the char-
acteristics without having to know the complete
details of the object.
These attributes form the necessary conditions for a
taxonomy to be useful, but they do not necessarily
identify the sufficient conditions. They can, however,
give guidance to researchers and represent foundations
that can be used for descriptive evaluations on the basis
of informed argument by developing convincing argu-
ments for a taxonomy’s utility (Hevner & Chatterjee,
2010, p. 119). We are not able at this time to give
sufficient conditions other than to say that a taxonomy is
useful if others use it. Clearly, this condition is tautolo-
gical. It is also correlated with design science research,
which seeks utility, not truth (Hevner et al, 2004). If this is
the only sufficient condition, however, then the only way
to evaluate a taxonomy’s usefulness is to observe its use
over time. We would like to have sufficient conditions
that
are
easier
to
apply
than
this
condition
and
that could be applied before putting a taxonomy into
use. However, such sufficient conditions are likely to
depend on the expected use of a taxonomy. For example,
one use of a taxonomy might be to help users navigate
through a knowledge domain. A sufficient condition
for this use might be related to how easy it is for the
user to find related objects grouped together in the
taxonomy. Another use might be to discover new things
about a domain. In this case, a sufficient condition
might be that some observations can be made about the
domain that were not possible before. We could argue
that the necessary conditions given previously are also
sufficient but we feel that these conditions are not
adequate for sufficiency. We leave this as an area for
future research.
A taxonomy development method should have certain
qualities. The goal of such a method is to develop a taxo-
nomy with a set of dimensions each consisting of a set
of characteristics that sufficiently describes the objects in
a specific domain of interest. The method should have
the following qualities:
 It takes into consideration alternative approaches to
taxonomy development. Because several approaches to
taxonomy development are used, and no single app-
roach has been determined to be ‘best’, any method
must be flexible enough to allow for the selection of an
approach or combination of approaches that is appro-
priate for the domain being studied.
 It reduces the possibility of including arbitrary or ad
hoc dimensions and characteristics in the taxonomy.
Any taxonomy should have dimensions and character-
istics based on conceptual and/or empirical grounds.
Arbitrary or ad hoc dimensions and characteristics
should be avoided and a taxonomy development
method must support this goal.
 It can be completed in a reasonable period of time. Any
method must have a way of determining when it is
finished. There must be an ending condition in the
taxonomy development method that says when to
stop, and this ending condition must be reachable in a
reasonable amount of time.
 It must be straightforward to apply. Because taxo-
nomies are developed by researchers with different
levels of understanding of the taxonomy development
literature, any method must be relatively easy to
understand and apply without reference to the litera-
ture.
 It must lead to a useful taxonomy. Since our goal is to
develop useful taxonomies, any method must accom-
plish this goal.
Our problem statement can thus be stated as follows:
Define a method for developing taxonomies such that
 The resulting taxonomies satisfy the definition of a
taxonomy given previously.
 The resulting taxonomies have the qualitative attri-
butes listed previously.
 The method has the qualities listed previously.
Taxonomy development method
We now present our method for developing taxonomies
of objects in a domain of interest. Following the design
science paradigm, we are building an artifact that is a
method, the purpose of which is to build (develop)
another artifact (a taxonomy). Our method is intended to
provide guidance
for researchers during
the design
process of taxonomy development. We follow the defini-
tion of March & Smith (1995, p. 257), who define a
method as a ‘set of steps (an algorithm or guideline) used
to perform a task’. Our method should provide a guide-
line to support the process of developing taxonomies in a
domain of interest, that is, it should provide ‘means to
reach desired ends while satisfying laws in the problem
environment’ (Hevner et al, 2004, p. 88). For an earlier
version of our method see Nickerson et al (2009).
A method for taxonomy development
Robert C. Nickerson et al
342
European Journal of Information Systems

## Page 8

Meta-characteristic
The development of a taxonomy involves determining
the characteristics of the objects of interest. The choice of
the characteristics in a taxonomy is a central problem in
taxonomy development. The characteristics could be
based on a theory but in reality any ‘theory’ is often
implicit (Aldenderfer & Blashfield, 1984). The researcher
must avoid, however, the situation of ‘naı¨ve empiricism’
in which a large number of related and unrelated
characteristics are examined in the hope that a pattern
will emerge (Aldenderfer & Blashfield, 1984, p. 20).
To avoid this situation and provide a basis for identi-
fying the characteristics of the taxonomy, we specify
a meta-characteristic at the beginning of the taxonomy
development process. The meta-characteristic is the most
comprehensive characteristic that will serve as the basis
for the choice of characteristics in the taxonomy. Each
characteristic should be a logical consequence of the
meta-characteristic.
The choice of the meta-characteristic should be based
on the purpose of the taxonomy. For example, assume
that the researcher is trying to classify computer plat-
forms (hardware and operating system) into a taxonomy.
If the researcher’s purpose is to distinguish platforms
based on processing power, then the meta-characteristic
is the hardware and software characteristics, such as CPU
power, memory, and operating system efficiency that
impact measures of power such as speed and capacity. On
the other hand, if the researcher’s purpose is to dis-
tinguish among computer platforms based on how users
use them, then the meta-characteristic is the capability
of the platform to interact with users, such as the maxi-
mum number of simultaneously running applications
and the user interface.
The purpose of the taxonomy should, in turn, be based
on the expected use of the taxonomy and thus could be
defined by the eventual users of the taxonomy. The
design process could involve first identifying the user(s)
of the taxonomy who then specify the projected use of
the taxonomy, either explicitly or implicitly. Explicitly,
the potential use of a taxonomy could be elicited from
actual users using elicitation techniques similar to those
employed in requirements analysis (see, e.g., Goguen &
Linde, 1993). Alternatively, the researcher could project
who the users could be and decide, based on experience,
what use the users could make of the taxonomy. In the
computer platform example in the previous paragraph,
the researcher may wish to develop a taxonomy to be
used by customers purchasing computers (the users of the
taxonomy). If the researcher projects that these custo-
mers will be technology-savvy individuals interested in
processing power, then the first taxonomy would be
appropriate. On the other hand, if the researcher deter-
mines that the customers will be application-savvy
individuals interested in how they can use the computer,
then the second taxonomy would be appropriate.
The choice of the meta-characteristic must be done
carefully as it impacts critically the resulting taxonomy.
Although
ideally
the
meta-characteristic
should
be
specified before determining the characteristics in the
taxonomy our experience has been that the meta-
characteristic sometimes does not become clear until
part way through the taxonomy development process
when we ask ourselves what the overall ‘theme’ is of the
characteristics that we have proposed. We have found
that this exercise often leads to a clear statement of the
meta-characteristic and to eliminating some character-
istics and identifying new characteristics.
We
see
meta-characteristics
appearing
in
research
that develops taxonomies for various purposes, although
they are not identified as such. For example, Nickerson
(1997) develops a taxonomy of collaborative applications
based on the meta-characteristic of
communication
among group members. Williams et al (2008) choose
two meta-characteristics – design and objectives – in
developing their taxonomy of digital services. Leem et al
(2004) develop a classification scheme for mobile busi-
ness models starting with the meta-characteristic of
‘business players’.
Ending conditions
The method that we describe is iterative and thus must
have conditions to determine when to terminate. These
conditions are both objective and subjective. A funda-
mental objective ending condition is that the taxonomy
must satisfy our definition of a taxonomy, specifically
that it consists of dimensions each with mutually
exclusive
and
collectively
exhaustive
characteristics.
We have identified eight additional objective ending
conditions listed in Table 2. Some of these conditions
are adapted from Sowa & Zachman’s (1992) rules for
their IS architecture framework. This list is not exhaustive
and future research may identify additional objective
ending conditions. An initial step for the researcher is to
decide which of these or other objective conditions will
be used to determine when to terminate the method.
Subjective ending conditions also need to be exam-
ined. Previously, we noted that necessary conditions for a
useful taxonomy are that it is concise, robust, compre-
hensive, extendible, and explanatory. These conditions
are the minimal subjective ones that must be met for the
method to terminate. Table 3 lists these subjective
conditions with questions that the researcher could ask
about each condition. The researcher can refer to the
previous
discussion
of
these
conditions
for
further
guidance. The researcher may wish to add more sub-
jective conditions to these based on the researcher’s
particular view. The researcher needs to be able to argue
that all subjective conditions have been met before
terminating the method.
Depending on the chosen ending conditions, the
method may generate somewhat different taxonomies,
which is consistent with the design science philosophy of
searching for useful, not necessarily optimal, solutions
(Hevner et al, 2004). Our method can be extended to
select a more useful taxonomy among multiple choices
A method for taxonomy development
Robert C. Nickerson et al
343
European Journal of Information Systems

## Page 9

and even merge multiple taxonomies into one if needed.
We leave this for future research.
Taxonomy development method
We are interested in the characteristics of the objects
being examined, not their evolutionary heritage. Thus,
our approach to developing a taxonomy is phenetic,
not cladistic. We find that Bailey’s (1984) three-level
indicator model provides a basis for a method for
developing
taxonomies
as
it offers
alternative app-
roaches that involve both conceptualization/deduction
and empiricism/induction. Bailey, however, implies that
taxonomy development takes one approach or the
other – the ‘classical strategy’ of conceptual to empirical
or the ‘opposite strategy’ of empirical to conceptual
(Bailey, 1994, pp. 31–32). Bailey’s approach is also static
in the sense that it terminates after applying one or the
other strategy and does not cycle back for additional
applications of the strategies. Thus, Bailey’s approach is
not consistent with the Hevner et al (2004, p. 88) design
science research guideline that asks for ‘design as a search
process’.
Our method goes beyond Bailey’s concept to com-
bine the conceptualization/deduction and empiricism/
induction strategies into a single method that encourages
the researcher to use the strategies in an iterative manner
to best reach a useful taxonomy. In addition, our method
includes specific ending conditions that test the taxo-
nomy as it is being developed. This approach is consistent
with the design science ‘generate/test cycle’ described by
Table 2
Objective ending conditions
Objective ending condition
Comments
All objects or a representative sample of objects have been
examined
If all objects have not been examined, then the additional objects
need to be studied
No object was merged with a similar object or split into
multiple objects in the last iteration
If objects were merged or split, then we need to examine the impact
of these changes and determine if changes need to be made in the
dimensions or characteristics
At least one object is classified under every characteristics of
every dimension
If at least one object is not found under a characteristic, then the
taxonomy has a ‘null’ characteristic. We must either identify an
object with the characteristic or remove the characteristic from the
taxonomy
No new dimensions or characteristics were added in the last
iteration
If new dimensions were found, then more characteristics of the
dimensions may be identified. If new characteristics were found,
then more dimensions may be identified that include these
characteristics
No dimensions or characteristics were merged or split in the
last iteration
If dimensions or characteristics were merged or split, then we need
to examine the impact of these changes and determine if other
dimensions or characteristics need to be merged or split
Every dimension is unique and not repeated (i.e., there is no
dimension duplication)
If dimensions are not unique, then there is redundancy/duplication
among dimensions that needs to be eliminated
Every characteristic is unique within its dimension (i.e., there
is no characteristic duplication within a dimension)
If characteristics within a dimension are not unique, then there is
redundancy/duplication in characteristics that needs to be elimi-
nated. (This condition follows from mutual exclusivity of character-
istics.)
Each cell (combination of characteristics) is unique and is not
repeated (i.e., there is no cell duplication)
If cells are not unique, then there is redundancy/duplication in cells
that needs to be eliminated
Table 3
Subjective ending conditions
Subjective ending
condition
Questions
Concise
Does the number of dimensions allow the taxonomy to be meaningful without being unwieldy or
overwhelming? (A possible objective criteria for this condition is that the number of dimensions falls in the
range of seven plus or minus two; Miller, 1956.)
Robust
Do the dimensions and characteristics provide for differentiation among objects sufficient to be of interest?
Given the characteristics of sample objects, what can we say about the objects?
Comprehensive
Can all objects or a (random) sample of objects within the domain of interest be classified? Are all
dimensions of the objects of interest identified?
Extendible
Can a new dimension or a new characteristic of an existing dimension be easily added?
Explanatory
What do the dimensions and characteristic explain about an object?
A method for taxonomy development
Robert C. Nickerson et al
344
European Journal of Information Systems

## Page 10

Hevner et al (2004, pp. 88–89). Finally, our method adds
the important concept of meta-characteristic that Bailey
does not identify explicitly or implicitly.
Figure 1 shows the method that we propose. Steps in
this figure are numbered for later reference. A step-by-
step explanation follows the figure.
The first step is to identify the meta-characteristic,
which, as discussed previously, is based on the purpose of
the taxonomy and in turn based on the users and their
expected use of the taxonomy. Next, the conditions that
end the process need to be determined. As discussed
previously, there are both objective and subjective ending
conditions. The researcher has a number of objective
conditions that can be applied (Table 2). The subjective
ones are the most difficult to identify and to apply.
Table 3 provides initial guidance but the experience of
the researcher will have an impact on the selection of
subjective conditions. In the case of multiple researchers
developing a taxonomy, various collaborative techni-
ques, including the Delphi method, could be used to
determine these conditions.
After these steps the researcher can begin with either an
empirical approach or a conceptual approach. The choice
of which approach to use depends on the availability
of data about objects under study and the knowledge
of the researcher about the domain of interest. If little
data are available but the researcher has significant
understanding of the domain, then starting with the
conceptual-to-empirical
approach
would
be
advised.
On the other hand, if the researcher has little under-
standing of the domain but significant data about the
objects is available, then starting with the empirical-to-
conceptual approach is appropriate. If the researcher has
both significant knowledge of the domain and significant
data available about the objects, then the researcher will
have to use individual judgment to decide which app-
roach is best. In the fourth case, where the researcher has
little knowledge of the domain and little data available,
the researcher should investigate the domain of interest
more before attempting to develop a taxonomy for it.
In subsequent iteration the researcher may choose to use
a different approach in order to view the taxonomy from
a different perspective and possibly gain new insight
about the taxonomy.
In the empirical-to-conceptual approach, the research-
er identifies a subset of objects that he/she wishes
to classify. These objects are likely to be the ones with
which the researcher is most familiar or that are most
easily accessible, possibly through a review of the lite-
rature. The subset could be a random sample, a syste-
matic sample, a convenience sample, or some other type
of sample. Next, the researcher identifies common cha-
racteristics of these objects. The characteristics must
be
logical
consequences
of
the
meta-characteristic.
Thus, the researcher starts with the meta-characteristic
and identifies characteristics of the objects that follow
from the meta-characteristic. The characteristics must,
however, discriminate among the objects; a characteristic
1. Determine meta-characteristic
No
2. Determine ending conditions
End
3. Approach?
Yes
Empirical-to-conceptual
Conceptual-to-empirical 
4c. Conceptualize (new)
characteristics and dimensions of objects
5c. Examine objects for these
characteristics and dimensions
6c. Create (revise) taxonomy
4e. Identify (new)
subset of objects  
5e. Identify common characteristics
and group objects  
 6e. Group characteristics into
dimensions to create (revise)
taxonomy  
7. Ending conditions met?
Start
Figure 1
The taxonomy development method.
A method for taxonomy development
Robert C. Nickerson et al
345
European Journal of Information Systems

## Page 11

that has the same value for all or nearly all objects is of
no use in the taxonomy even if it does follow from the
meta-characteristic (Anderberg, 1973). The knowledge
and intuition of the researcher or other experts will be
needed to identify the characteristics. If multiple resea-
rchers or experts are working on the taxonomy, a group
methodology, such as the Delphi method, could be
employed. In the process, characteristics may be pro-
posed that turn out not to be relevant and thus can be
eliminated after further analysis.
Once a set of characteristics has been identified, they
can be grouped formally using statistical techniques
or informally using a manual or graphical process. The
resulting groups form the initial dimensions of the
taxonomy. This grouping involves creating ‘conceptual
labels’ (Bailey, 1994, p. 32) for sets of related character-
istics, that is, for the dimensions. Each dimension
contains characteristics that are mutually exclusive and
collectively exhaustive. For example, dimension D1 may
group characteristics C11 and C12 and dimension D2 may
group characteristics C21, C22, and C23. All objects have
one and only one of the characteristics C1j in dimension
D1 and one and only one of the characteristics C2j in
dimension D2. Some dimensions may be dichotomous
(e.g., D1) and some may not be (e.g., D2). This process is
based on the (limited) empirical data that has been
gathered about objects and the deductive conceptuali-
zation of the researcher. The result of this process is an
initial taxonomy based on an empirical-to-conceptual
approach.
In the conceptual-to-empirical approach, the resea-
rcher begins by conceptualizing the dimensions of the
taxonomy without examining actual objects. This process
is based on the researcher’s notions about how objects
are similar and how they are dissimilar. Since this is
a deductive process, little guidance can be given other
than to say that the researcher uses his/her knowledge of
existing
foundations,
experience,
and
judgment
to
deduce what he/she thinks will be relevant dimensions.
Each dimension contains characteristics that must be
logical consequences of the meta-characteristic. Thus, a
test of the appropriateness of a dimension is whether
its characteristics follow from the meta-characteristic.
In the process, the researcher may propose dimensions
that are not appropriate and thus can be eliminated. The
researcher then examines objects for these dimensions
and characteristics. Are there objects that have each
of the characteristics in each dimension? If not, then the
dimension may not be appropriate. As before, each
dimension must contain characteristics that are mutually
exclusive and collectively exhaustive. The result of this
process is an initial taxonomy based on a conceptual-to-
empirical approach.
At the end of either of these steps, the researcher asks
if the ending conditions have been met with the current
version of the taxonomy. Both objective and subjective
conditions must be checked. Since this is the first itera-
tion, it is likely that none of the objective conditions will
be met so the process is repeated. In subsequent iterations
the objective conditions must be evaluated and if not
met, the process is repeated. If the objective conditions
have been met, then the subjective conditions need to be
examined.
Evaluating
these
conditions
requires
the
insight, experience, and skill of the researcher. Examples
of heuristics that could be used were given previously. If
all the subjective conditions have not been met, then the
process is repeated.
In repeating the method, the researcher must again
decide which approach to use. Since new objects may
have been identified or new domain knowledge may
have been obtained in the previous iteration, the resea-
rcher can use the previous heuristics anew to decide
which approach to apply in the next iteration. In the
empirical-to-conceptual case the researcher examines
new objects to determine whether the existing character-
istics are sufficient to describe them or if new character-
istics and possibly new dimensions are needed. As before,
statistical techniques can be used to aid in this process.
This process could even result in the elimination of
some dimensions and/or characteristics if they are deter-
mined not to be applicable. The result is the next version
of the taxonomy. In the conceptual-to-empirical case the
researcher reviews the previous taxonomy to try to
identify additional conceptualizations that might not
have been previously identified. In the process new
characteristics may be deduced that fit into existing
dimensions or new dimensions may be conceptualized
each with their own set of characteristics. It may even be
the case that some dimensions or characteristics are
eliminated or combined so that fewer dimensions and/or
characteristics result. The researcher examines empirical
cases using the new characteristics and dimensions to
determine their usefulness in classifying objects. The
result is the next version of the taxonomy. As before, the
researcher checks if the ending conditions (objective and
subjective) have been met and either terminates the
process or repeats it.
We note that with each iteration of the design process,
new dimensions may be added and existing dimensions
may be eliminated. These are the processes of substruc-
tion and reduction, respectively, described previously and
discussed by Bailey (1994, p. 24).
It is important throughout the process that the resea-
rcher remembers that the taxonomy must be explana-
tory, not descriptive. That is, it must contain dimensions
and characteristics that do not describe objects in
complete detail but, rather, provide useful explanations
of the nature of the objects under study or of future
objects.
Upon completion of the method (i.e., after the design
science building phase), the resulting taxonomy needs to
be
evaluated
for
its
usefulness
(the
design
science
evaluation phase). As we explained earlier, determining
sufficient
conditions
for
usefulness
is
difficult
and
evaluating usefulness may come down to seeing if others
use it. Before this takes place, however, we can speculate
A method for taxonomy development
Robert C. Nickerson et al
346
European Journal of Information Systems

## Page 12

on potential use of the taxonomy. Given a user or users
and the purpose of the taxonomy, can the user’s purpose
be satisfied with the taxonomy? To answer this question,
we could query users about their potential use of
the taxonomy, or if users are not available, we could
evaluate what the taxonomy tells the users in relation to
the purpose of the taxonomy.
We do not propose that our approach is the best or only
taxonomy development method, only that it provides
guidance during the process of taxonomy development.
Further, it follows from the taxonomy development
literature and satisfies the criteria listed previously in
our problem statement. Specifically,
 It takes into consideration alternative approaches
to taxonomy development. Our method uses both
an empirical/inductive approach and a conceptual/
deductive approach and allows the researcher to decide
what approach to use at each pass through the
method.
 It reduces the possibility of including arbitrary or ad
hoc dimensions and characteristics in the taxonomy.
Our method requires that the characteristics and
dimensions be developed using a systematic process,
not developed in an ad hoc way.
 It can be completed in a reasonable period of time. Our
method is designed to reach closure in a few repeti-
tions of the method, although this requires the insight
of the researcher. If the researcher finds that the
taxonomy is not converging on the ending con-
ditions in each repetition of the method, then the
researcher must take steps to rectify the situation,
possibly starting again from scratch.
 It is straightforward to apply. Our method provides a
specific set of steps that a trained researcher should be
able to apply without additional reference to the
taxonomy development literature.
 It leads to a useful taxonomy. This criteria is the
hardest to determine if it has been satisfied. As
discussed previously, a useful taxonomy must meet
certain necessary conditions. The subjective ending
conditions of the method include these conditions.
These conditions, however, are not necessarily suffi-
cient for a useful taxonomy. Unless more specific
sufficient conditions can be identified, the only way
to determine if the resulting taxonomy is useful is to
observe its use by others over time. Asking users to
evaluate the usefulness of a taxonomy is one way of
evaluating the taxonomy. If a taxonomy turns out not
to be useful, then the process needs to be restarted,
perhaps with a different meta-characteristic.
Development of a taxonomy of mobile
applications
To demonstrate the efficacy of the method described
previously, we use it to develop a taxonomy of mobile
applications. In the design science paradigm we are
evaluating the artifact (method) built previously by using
it to develop another artifact, specifically a model, and
evaluating that artifact (taxonomy) by using it to classify
objects of interest. For less detailed discussions of the
taxonomy developed here see Nickerson et al (2007) and
Nickerson et al (2009).
We define a mobile application as a use of a mobile
technology by an end-user for a particular purpose, for
example, purchase a ring tone, check a weather fore-
cast, transfer funds at a bank, make an airline reservation
and so on. Mobile applications are provided by mobile
services that have the infrastructure necessary to deliver
the application. A mobile service, however, may provide
several different applications under the umbrella of one
service. For example, a mobile service may provide infor-
mation about popular music and sell MP3 music files. For
this paper, we view these as two different applications –
one, an informational application, and the other, a trans-
actional application – both provided by one service.
A number of taxonomies in the mobile/wireless area
have been proposed. A review and critique of some
taxonomies presented in the early stages of the mobile
era and predominantly written in German can be found
in Lehmann & Lehner (2002). More recent papers include
Dombroviak & Ramnath (2007), which gives a taxonomy
of what the authors call ‘mobile pervasive’ applications,
Leem et al (2004) and Abdelaal & Ali (2007), which
presents taxonomies of mobile business models, Nysveen
et al (2005) and Heinonen & Pura (2006), which describe
taxonomies of mobile services, Williams et al (2008),
which gives a taxonomy of digital (not just mobile)
services,
Kemper
&
Wolf
(2002),
which
presents
a
taxonomy dealing with mobile application development,
and Dobson (2004), which gives a taxonomy of location
in pervasive computing.
The users of the taxonomy we develop are researchers
and developers of mobile applications. In characterizing
mobile applications, this user group is interested in high-
level characteristics of the user interaction with mobile
applications. They are not interested in technical char-
acteristics of the application, such as type of mobile
device used or speed of network connection, nor in how
the user uses technology, such as keypads and touch
sensitive screens, with the application. Indeed, mobile
technology is constantly evolving and any taxonomy
based on it may quickly be out of date. In addition, this
user group is not interested in characterizing the pur-
poses
of
mobile
applications,
although
developing
a taxonomy with this goal may be beneficial. This user
group wants to be able to use the taxonomy to identify
the characteristics of how users interact with applications
currently or may interact with applications in the future
at a higher level of abstraction than the physical inter-
action with the application. Specifically, the purpose
of
our
taxonomy
is
to
distinguish
among
mobile
applications based on how the application user interacts
at a high level with the application. Such a taxonomy will
help researchers and developers identify whether new
applications are truly unique from the user’s perspective
A method for taxonomy development
Robert C. Nickerson et al
347
European Journal of Information Systems

## Page 13

and where applications do not exist in the taxonomy
suggesting opportunities for new applications. Thus, the
meta-characteristic
for
the
taxonomy
development
process is the high-level interaction between the user
and the application.
We now demonstrate the application of the method
shown in Figure 1 using the numbered steps in the figure.
Step 1:
Meta-characteristic: High-level interaction bet-
ween the application user and the application.
Step 2:
Ending conditions: The method will end when
both objective and subjective conditions have
been met. For simplicity in this example, we
will use only two objective ending conditions
from Table 2, specifically, that no new dimen-
sions are added in the last iteration and no
additional applications need to be examined.
Subjectively, the method will end when all the
conditions in Table 3 are met, that is, when the
taxonomy is determined to be concise, robust,
comprehensive, extendible, and explanatory.
Iteration 1:
Step 3:
Approach: We decide to use the empirical-to-
conceptual approach first because we have
identified some mobile applications from pre-
vious research in the mobile area.
Step 4e:
We select the following convenience sample of
mobile applications from the literature (Varsh-
ney & Vetter, 2002; Ngai & Gunasekaran,
2007):
 Mobile voice communications.
 Mobile messaging.
 Mobile TV.
Step 5e:
We identify the following user interaction
characteristics
in
these
applications
based
on
our
understanding
of
the
applications
and identify which application has each char-
acteristic:
 User
interacts
with
application
synchro-
nously.
 User interacts with application asynchro-
nously.
 Information flows from the application to
the user.
 Information flows from the user to the
application and also from the application
to the user.
For example, the mobile TV application in-
volves synchronous user interaction and in-
formation flowing from the application to the
user. All these characteristics follow from the
meta-characteristic in the sense that they are
aspects of the high-level user interaction with
the application.
Step 6e:
Because the number of characteristics is small,
we can group these characteristics manually
into the following dimensions to form our first
taxonomy:
 Temporal dimension: synchronous user in-
teraction and asynchronous user interaction
characteristics.
 Communication dimension: informational
(information flows only from application to
user) and interactive (information flows both
from application to user and from user to
application) characteristics.
In the notation used previously for our definition of
taxonomy, our first taxonomy T1 consists of dimension
D1 ¼ Temporal
with characteristics
C11 ¼ Synchronous
and C12 ¼ Asynchronous, and D2 ¼ Communication with
characteristics C21 ¼ Informational and C22 ¼ Interactive,
or more simply:
T1¼ fTemporal ðSynchronous; AsynchronousÞ;
Communication ðInformational; InteractiveÞg
Table 4 shows the classification of the applications
examined in this iteration in this taxonomy.
Step 7:
Ending conditions: Since two dimensions were
created in this iteration, the method must be
repeated. In addition, more mobile applica-
tions exist that need to be examined. We note,
however, that the taxonomy is concise, exten-
dible, and explanatory, but its limited number
of dimensions and characteristics may not be
robust, and it is not known if it is comprehen-
sive because more mobile applications exist
that need to be considered. At least one more
iteration is needed.
Iteration 2:
Step 3:
Approach: We decide to use the empirical-to-
conceptual approach again because we have
Table 4
Taxonomy of mobile applications after
Iteration 1
Applications
Temporal
Communication
S
AS
INF
INT
Mobile voice communications
X
X
Mobile messaging
X
X
Mobile TV
X
X
A method for taxonomy development
Robert C. Nickerson et al
348
European Journal of Information Systems

## Page 14

identified additional mobile applications from
previous research in the mobile area.
Step 4e:
We
select
the
following
sample
of
addi-
tional mobile applications from the literature
(Varshney & Vetter, 2002 and Ngai & Gunase-
karan, 2007):
 Purchasing location-based contents.
 Mobile inventory management.
 Product location and tracking.
 Mobile advertising.
 Mobile navigation.
Step 5e:
We identify the following user interaction cha-
racteristics in these applications based on our
understanding of the applications and identify
which application has each characteristic:
 Information flows from the application to
the user.
 User
engages
in
a
financial
transaction
through the application.
 User does not engage in a financial transac-
tion through the application.
For example, the purchasing location-based
contents
application
involves
synchronous
user interaction, information flowing from the
application to the user, and the user engaging in
a financial transaction. All these characteristics
follow logically from the meta-characteristic.
Step 6e:
We recognize that the first characteristic is an
additional characteristic in the communica-
tion dimension identified previously. Thus,
this dimension becomes:
 Communication dimension: informational
(information flows only from application to
user), reporting (information flows only from
user to application), and interactive (informa-
tion flows both from application to user and
from user to application) characteristics.
The other two characteristics can be grouped
into the following dimension:
 Transaction dimension: transactional (user
engages in financial transaction) and non-
transactional (user does not engage in finan-
cial transaction) characteristics.
At this point we have our second taxonomy:
T2¼ fTemporal ðSynchronous; AsynchronousÞ;
Communication ðInformational; Reporting; InteractiveÞ;
Transaction (Transactional, Non-transactional)g
Table
5
shows
the
applications
examined
so
far
classified in this taxonomy.
Step 7:
Ending conditions: Since one more dimension
was created in this iteration, the method must
be repeated. In addition, more mobile applica-
tions exist that need to be examined. We note,
however, that the taxonomy is concise, ex-
tendible,
and
explanatory,
but
its
limited
number
of
dimensions
and
characteristics
may not be robust and it is not known if it is
comprehensive because more mobile applica-
tions exist that need to be considered. At least
one more iteration is needed.
Iteration 3:
Step 3:
Approach: For the third iteration we decide
to use the conceptual-to-empirical approach in
order to get a different perspective on the
taxonomy.
Step 4c:
We conceive that some applications can interact
with anyone, that is, they are public, and some
applications can only be used by individuals
who have certain privileges such as those who
work for a company, that is, they are private. We
identify this as an access dimension and note
that it follows from the meta-characteristic:
Table 5
Taxonomy of mobile applications after Iteration 2
Applications
Temporal
Communication
Transaction
S
AS
INF
RP
INT
T
NT
Mobile voice communications
X
X
X
Mobile messaging
X
X
X
Mobile TV
X
X
X
Purchasing location-based contents
X
X
X
Mobile inventory management
X
X
X
Product location and tracking
X
X
X
Mobile advertisement
X
X
X
Mobile navigation
X
X
X
A method for taxonomy development
Robert C. Nickerson et al
349
European Journal of Information Systems

## Page 15

 Access dimension: public (can be used by
anyone) and private (use restricted to certain
individuals) characteristics
Step 5c:
We identify instances of these types of applica-
tion. For example, purchasing location-based
contents is a public application and mobile
inventory management is a private applica-
tion.
Step 6c:
Adding this dimension to the previous three
dimensions creates our next taxonomy:
T3¼ fTemporal ðSynchronous; AsynchronousÞ;
Communication ðInformational; Reporting; InteractiveÞ;
Transaction ðTransactional; Non-transactional),
Access ðPublic; PrivateÞg
Table 6 shows the applications identified previously
classified with this taxonomy.
Step 7:
Ending conditions: Since one dimension was
added in this iteration, we must repeat the
method. The taxonomy is concise, extendible,
and explanatory. However, the addition of
another
dimension
makes
the
taxonomy
more robust. At least one more iteration is
needed.
Iteration 4:
Step 3:
Approach: Since there are more applications
to
examine,
we
follow
the
empirical-to-
conceptual approach for this iteration.
Step 4e:
We select the following additional mobile
applications from the literature (Varshney &
Vetter, 2002; Ngai & Gunasekaran, 2007):
 Mobile games.
 Mobile entertainment services.
 Mobile social networking.
 Mobile communities.
Step 5e:
We identify the following user interaction
characteristics in these applications and iden-
tify which application has each characteristic:
 Application has a single user.
 Application has multiple users.
Although mobile applications can be used by
many users simultaneously, users may not be
aware of this characteristic and view their use of
the application as individual. With some appli-
cations, however, users may know that they are
part of a multiple-user community using the
application.
Step 6e:
We can group these characteristics manually
into the following dimension to form our next
taxonomy:
 Multiplicity dimension: individual (user ex-
periences the application as if he/she were
the sole user) and group (user views use of
the application as part of a group) character-
istics
At this point we have our next taxonomy:
T4¼ fTemporal ðSynchronous; AsynchronousÞ;
Communication ðInformational; Reporting; InteractiveÞ;
Transaction ðTransactional; Non-transactional),
Access ðPublic; PrivateÞ;
Multiplicity ðIndividual; GroupÞg
Table 7 shows all the applications identified so far
classified in this taxonomy.
Step 7:
Ending conditions: Since one more dimension
was created in this iteration, the method must
be
repeated.
We
note,
however,
that
the
taxonomy is concise, extendible, and explana-
tory, and more robust than before. At least one
more iteration is needed.
Table 6
Taxonomy of mobile applications after Iteration 3
Applications
Temporal
Communication
Transaction
Access
S
AS
INF
RP
INT
T
NT
PU
PR
Mobile voice communications
X
X
X
X
Mobile messaging
X
X
X
X
Mobile TV
X
X
X
X
Purchasing location-based contents
X
X
X
X
Mobile inventory management
X
X
X
X
Product location and tracking
X
X
X
X
Mobile advertisement
X
X
X
X
Mobile navigation
X
X
X
X
A method for taxonomy development
Robert C. Nickerson et al
350
European Journal of Information Systems

## Page 16

Iteration 5:
Step 3:
Approach: We decide to use the conceptual to
empirical because we feel that we can conceive
new dimensions.
Step 4c:
We
conceive
of
two
more
dimensions
of
mobile applications with characteristics related
to the meta-characteristic.
Some mobile applications may provide custo-
mized information or functionality based on
the user’s location, whereas other applications
may not depend on where the user is located.
The location dimension deals with whether the
location of the user is used to modify the
interaction of the application with the user:
 Location dimension: Location-based (applica-
tion uses the user’s location) and non-loca-
tion-based (application does not use the
user’s location) characteristics
Like the location dimension, some mobile
applications may adjust their information or
functionality based on an awareness of who
the user is, whereas other applications may
not
depend
on
the
user’s
identity.
The
identity dimension relates to whether the
identity of the user is used to modify the way
the application interacts with the user based
on the user’s identity:
 Identity dimension: Identity-based (applica-
tion uses the user’s identity) and non-iden-
tity-based (application does not use the user’s
identity) characteristics.
Step 5c:
We find a number of applications from our
original lists
with these characteristics. For
example, mobile purchasing of location-based
content is location-based but mobile games are
not, and mobile social networking is identity-
based but mobile entertainment services are not.
Step 6c:
Adding these two dimensions to the previous
five dimensions gives us our next taxonomy:
T5¼ fTemporal ðSynchronous; AsynchronousÞ;
Communication ðInformational; Reporting; InteractiveÞ;
Transaction ðTransactional; Non-transactional),
Access ðPublic; PrivateÞ;
Multiplicity ðIndividual; GroupÞ;
Location (Location-based, Non-location-based),
Identity (Identity-based, Non-identity-based)g
All the applications are classified in this taxonomy in
Table 8.
Step 7:
Ending conditions: Since we added two dimen-
sions in this iteration, we need to repeat the
method. In addition, other applications need to
be examined. The current taxonomy is concise,
extendible, and explanatory, and the addition of
two dimensions to a total of seven dimensions
makes the taxonomy robust. It is not known if it
is comprehensive because more mobile applica-
tions exist that need to be considered.
Iteration 6:
Step 3:
Approach: Since there are more applications to
examine, we follow the empirical-to-concep-
tual approach for this iteration.
Step 4e:
We identify additional applications from the
literature to consider (Varshney & Vetter, 2002;
Ngai & Gunasekaran, 2007):
 Mobile auctions and financial services.
 Mobile distance education.
 Mobile ticketing.
Table 7
Taxonomy of mobile applications after Iteration 4
Applications
Temporal
Communication
Transaction
Access
Multiplicity
S
AS
INF
RP
INT
T
NT
PU
PR
I
G
Mobile voice communications
X
X
X
X
X
Mobile messaging
X
X
X
X
X
Mobile TV
X
X
X
X
X
Purchasing location-based contents
X
X
X
X
X
Mobile inventory management
X
X
X
X
X
Product location and tracking
X
X
X
X
X
Mobile advertisement
X
X
X
X
X
Mobile navigation
X
X
X
X
X
Mobile games
X
X
X
X
X
Mobile entertainment services
X
X
X
X
X
Mobile social networking
X
X
X
X
X
Mobile communities
X
X
X
X
X
A method for taxonomy development
Robert C. Nickerson et al
351
European Journal of Information Systems

## Page 17

Steps 5e and 6e: We cannot identify any new character-
istics and dimensions from these appli-
cations. We group the new applications,
along with the previous applications,
using the existing characteristics and
dimensions as shown in Table 9.
Step 7:
Ending conditions: We have added no
new dimensions with this iteration and
we have examined a large sample of
mobile applications. Hence, the objec-
tive ending conditions are met. The
taxonomy is concise, extendible, robust,
and explanatory. With the considera-
tion of the additional applications, the
taxonomy appears to be comprehen-
sive. Thus, the taxonomy meets the
subjective
ending
conditions.
The
method ends at this point.
Our final taxonomy of mobile applications is given in
the previous formula (T5) and listed here:
 Temporal dimension: Synchronous and asynchronous
characteristics.
 Communication dimension: Informational, reporting,
and interactive characteristics.
 Transaction dimension: Transactional and non-trans-
actional characteristics.
 Access dimension: Public and private characteristics.
 Multiplicity dimension: Individual and group charac-
teristics.
 Location dimension: Location-based and non-location-
based characteristics.
 Identity dimension: Identity-based and non-identity-
based characteristics.
As noted previously our goal is to create useful taxo-
nomies. Our final test, then, is to examine the resulting
Table 8
Taxonomy of mobile applications after Iteration 5
Applications
Temporal
Communication
Transaction
Access
Multiplicity
Location
Identity
S
AS
INF
RP
INT
T
NT
PU
PR
I
G
LB
NLB
I
NI
Mobile voice communications
X
X
X
X
X
X
X
Mobile messaging
X
X
X
X
X
X
X
Mobile TV
X
X
X
X
X
X
X
Purchasing location-based contents
X
X
X
X
X
X
X
Mobile inventory management
X
X
X
X
X
X
X
Product location and tracking
X
X
X
X
X
X
X
Mobile advertisement
X
X
X
X
X
X
X
Mobile navigation
X
X
X
X
X
X
X
Mobile games
X
X
X
X
X
X
X
Mobile entertainment services
X
X
X
X
X
X
X
Mobile social networking
X
X
X
X
X
X
X
Mobile communities
X
X
X
X
X
X
X
Table 9
Taxonomy of mobile applications after Iteration 6
Applications
Temporal
Communication
Transaction
Access
Multiplicity
Location
Identity
S
AS
INF
RP
INT
T
NT
PU
PR
I
G
LB
NLB
I
NI
Mobile voice communications
X
X
X
X
X
X
X
Mobile messaging
X
X
X
X
X
X
X
Mobile TV
X
X
X
X
X
X
X
Purchasing location-based contents
X
X
X
X
X
X
X
Mobile inventory management
X
X
X
X
X
X
X
Product location and tracking
X
X
X
X
X
X
X
Mobile advertisement
X
X
X
X
X
X
X
Mobile navigation
X
X
X
X
X
X
X
Mobile games
X
X
X
X
X
X
X
Mobile entertainment services
X
X
X
X
X
X
X
Mobile social networking
X
X
X
X
X
X
X
Mobile communities
X
X
X
X
X
X
X
Mobile auctions and financial services
X
X
X
X
X
X
X
Mobile distance education
X
X
X
X
X
X
X
Mobile ticketing
X
X
X
X
X
X
X
A method for taxonomy development
Robert C. Nickerson et al
352
European Journal of Information Systems

## Page 18

taxonomy for its usefulness for the intended users and
the intended purpose. The users of the mobile applica-
tions taxonomy were projected to be researchers and
developers of mobile applications, and their purpose was
to distinguish among mobile applications based on how
the application user interacts with the applications at
a high level so as to help the taxonomy users identify
the uniqueness of newly developed mobile applications
and opportunities for new mobile applications. While the
former goal cannot be tested until new applications
appear, insight into the later goal can be gained by
examining the taxonomy in Table 9. We can make several
observations, including the following:
1. An approximately equal number of synchronous and
asynchronous applications are identified in Table 9,
implying that both modes have value. In the future,
new applications could be developed that run in
synchronous mode, but if network infrastructure is
experiencing high traffic load, these applications
could adjust to run in asynchronous mode.
2. Only one application in Table 9 is reporting, which
may be because the current needs of users for reporting
are being met by fixed devices. In the future, however,
such requirements may move to mobile devices. Thus,
more research and development could be done in
designing mobile applications that have the reporting
characteristic.
3. Most applications in Table 9 are non-transactional,
which may be because financial transactions, such as
online payments, are difficult with mobile devices.
There may be opportunities for research and develop-
ment into technology that facilitates mobile transac-
tions, such as mobile payment systems.
4. Only two private applications are in Table 9, which
could be because most mobile applications today are
B2C with public access. There may be opportunities
for research and development in mobile B2B or B2E
applications, which would have private access.
5. Table 9 includes only four group applications, which
means that there may be opportunities to develop new
group applications.
6. Although there are fewer location-based applications
than non-location-based applications in Table 9, the
difference is small. Thus, both types of applications
have value and future applications may be designed
with either approach.
7. Identity-based and non-identity based applications
are almost equally balanced in Table 9, implying that
both types of applications may be developed in the
future.
8. A number of voids can be found in the taxonomy.
For example, there are no applications that have the
combined characteristics of reporting, non-transac-
tional, private, and group. An opportunity may exist
for applications to fill this and other voids. For exam-
ple, an application for older adults might be developed
that allows users to report wellness and other information
about their lives to a group of geriatric friends who
they may not be able to meet face to face.
Discussion
This paper has presented a method for taxonomy deve-
lopment that is based on the taxonomy development
literature in other disciplines. The method is a hybrid of
methods used for typology development (conceptual)
and methods used for taxonomy development (empiri-
cal). The artifact resulting from applying our method can
be thought of as a hybrid of a typology and a taxonomy.
It could be called a classification, framework, typology,
taxonomy, or some other term, although we have chosen
to call it a taxonomy because our literature survey indi-
cated that this term is the most commonly used one in
papers that develop this type of artifact. By presenting
a hybrid approach resulting in hybrid taxonomies, we are
providing a method that results in taxonomies that are
likely to be more broadly useful than those that come
from more restricted approaches.
Our method does not identify an ideal type as is the
expected result in traditional typology development.
Likewise, our method does not result in a purely con-
structed type as in taxonomy development. Rather, our
method takes a pragmatic approach to create an artifact
that combines elements of both ideal and constructed
types. We do not look at the effectiveness of individual
elements classified in the taxonomy, as proposed by
Doty et al (1993) in their discussion of ideal types and
organizational configurations, but rather at the overall
effectiveness of a resulting taxonomy to classify objects in
a domain.
The flexibility of our method allows the researcher to
develop taxonomies without the limitations imposed by
traditional typology or taxonomy development. The
artifacts resulting from our method are likely to be more
comprehensive and more extendable (important char-
acteristics of a useful taxonomy) than those resulting
from traditional methods. Traditional typologies, with
their emphasis on ideal types, may be less comprehensive
and be harder to extend due to the difficulty in identi-
fying ideal types. Traditional taxonomies, with their
emphasis on constructed types, may also be less compre-
hensive and be difficult to extend due to their reliance on
empirical cases. By combining the two approaches we
allow the researcher to use a mixture that best serves the
researcher’s needs.
Our method is derived from the taxonomy develop-
ment literature in other disciplines, most notably the
social sciences. It follows from Bailey’s (1984) ‘three-level
model’ but goes significantly beyond that model by
including alternative methods (conceptual to empirical
and empirical to conceptual) that can be repeated in
different combinations.
The iterative nature of our
method allows it to add/split and remove/merge dimen-
sions and characteristics as it converges on an artifact
that is at the same time concise and robust. Our method
also includes the important concept of a meta-characteristic
A method for taxonomy development
Robert C. Nickerson et al
353
European Journal of Information Systems

## Page 19

and objective and subjective ending conditions, elements
that are not found in Bailey’s approach. Thus our
method, while related to Bailey’s, is different and a
significant contribution to the research in taxonomy
development.
Even with the method that we propose the judgment
of the researcher is required. The selection of the
meta-characteristic, the determination and application
of the ending conditions, the decision of which path
(empirical to conceptual or conceptual to empirical) to
take at each iteration, the identification of object
subsets, the conceptualization of characteristics and
dimensions, and other steps in the method all require
human judgment. Indeed, in some cases conflicting
criteria may have to be resolved by the researcher, such
as potential conflicts in the necessary criteria for a
taxonomy to be useful. We have provided guidelines and
heuristics to help the researcher, but these do not
supplant the researcher’s expertise and judgment. Some
tools may help, such as statistical cluster analysis for the
examination of empirical cases, but the researcher
must make the final determination of the taxonomy’s
structure.
Researchers can use our method to develop taxonomies
in different domains. Because the method is founded
on established concepts about taxonomy development
and has certain desirable qualities, researchers will have
a high degree of confidence that taxonomies developed
using this method will be useful to them and to others.
We have demonstrated the use of the method in only
one domain, but we have used it in other domains, and
we are confident that the method can be applied in a
wide range of domains.
We have proposed our method for use in developing
taxonomies in IS and have illustrated it with an example
from this discipline because it is the discipline with
which we are most familiar. There is nothing unique in
our method, however, to IS. Indeed, our problem state-
ment for taxonomy development is not specific to IS, and
no steps in our method apply only to IS. Investigation
of the use of our method in other areas is a potentially
fruitful area for future research. We speculate that this
research is likely to indicate the general applicability of
our method, and, if so, this may be the most significant
contribution of this paper.
The implications of our method for researchers is that
it provides an approach to taxonomy development that
is neither intuitive nor ad hoc, as we found was the case
in many papers that we surveyed, but rather deliberate
and planned. Researchers can be reasonably confident
that the taxonomies developed using our method will
meet their needs if not exactly then at least closely.
Readers of papers that present taxonomies developed
using our method can also be reasonably confident that
the taxonomy presented was developed in an estab-
lished way.
Although we have presented only one example of
the use of our method in taxonomy development in
this paper, we have used it to develop other taxonomies
and to critique published taxonomies and typologies.
We have also taught our method to other researchers
who have used it to develop taxonomies for their
research (Geiger et al, 2011; Krug et al, 2012). Continued
efforts in these endeavors appear to be promising.
Summary and conclusion
This paper has examined the question of taxonomy
development from several angles. First, it looked at a
range of literature and concluded that, whereas many IS
researchers have found taxonomies are useful, often the
process of developing a taxonomy in IS is ad hoc (unlike
taxonomy development in business or management-
related outlets, which tend to use more formal app-
roaches), and thus a method for taxonomy development
that researchers can use in place of an ad hoc app-
roach may be beneficial. Second, the paper defined the
problem of taxonomy development, presenting necessary
conditions for a taxonomy to be useful and requisite
qualities of a taxonomy development method. Third, the
paper presented a method for developing taxonomies
based on well-established literature in taxonomy devel-
opment and showed that the method had the requisite
qualities. Fourth, the paper demonstrated the efficacy of
the method by developing a taxonomy in an IS domain.
The approach that the paper took followed the design
science paradigm by first building a method for taxo-
nomy development, then evaluating the method by
using it to build a taxonomy (artifact), and finally
evaluating the taxonomy by using it to classify objects
in the domain.
The most important contribution of this paper is
the method that we present for developing taxonomies.
With this contribution we address the dichotomy of
design science research, since our method supports
design science researchers during their research activities
(design as a process) in order to develop useful taxo-
nomies (design as an artifact). Our method contributes to
the knowledge base of IS research, that is, the scientific
foundations from which it can be drawn when develop-
ing new taxonomies. The method addresses the pro-
cess of taxonomy development and provides guidance
during the design science build/evaluate cycle of deve-
loping taxonomies and evaluating them against a set of
necessary conditions for usefulness.
Future research in taxonomies and taxonomy develop-
ment in IS can take a number of directions. One is to
investigate the
question
of sufficient conditions
for
a useful taxonomy, a question that was identified pre-
viously in this paper. Along with this question goes the
question of whether a useful taxonomy has a minimal
number of dimensions. Fundamental to the method
we present in this paper is the concept of a meta-
characteristic. How to determine the appropriate meta-
characteristic for a taxonomy needs further investigation.
Determining and applying ending conditions in our
taxonomy development method requires some subjective
A method for taxonomy development
Robert C. Nickerson et al
354
European Journal of Information Systems

## Page 20

evaluation. Investigating ways that these conditions can
be made more objective is worthy of further investigation.
As we have noted, there is no one best taxonomy. We find
further arguments for this in the design science founda-
tions, which underline that the search for an optimal
design is intractable. In fact, multiple taxonomies may be
developed for a domain even when starting with the same
meta-characteristic. How to compare different taxonomies
for a given domain to determine which, if any, is best is
an open question. The method that we present results in
a single taxonomy. An alternative method would be to
develop several, possibly
overlapping taxonomies
for
different subsets of a domain. These taxonomies could
come from a single researcher or from different researchers
looking at the same domain. Then the question of how
to merge the taxonomies becomes important. This avenue
of research could also lead to investigation of group
taxonomy development and whether a software tool,
perhaps employing expert collaboration using the Delphi
or some other method, might be useful. As we have
pointed out, taxonomies are not static but change over
time as new objects that may or may not fit into an
existing taxonomy are developed or identified. Addressing
this increased diversity of objects in taxonomy modifica-
tion is another area for future research. Finally, applying
the method
in
this
paper
to
various
domains and
investigating the resulting taxonomies will be an ongoing
area for research.
About the authors
Robert C. Nickerson is a Professor of Information
Systems at San Francisco State University and Chair
of the Department of Information Systems from 2006 to
2012. His current research interests include taxonomies
and taxonomy development in information systems,
wireless/mobile systems, electronic commerce systems,
and crowdsourcing. He has been a regularly invited
professor at several European universities.
Upkar Varshney is an Associate Professor of CIS at
Georgia State University, Atlanta. His current interests
include mobile and wireless technologies, healthcare
technologies, pervasive computing, and m-commerce,
and he has authored numerous papers. He chaired the
International Pervasive Health Conference in 2006 and
program chaired AMCIS in 2009.
Jan Muntermann is a Professor and Chair of Electronic
Finance and Digital Markets at the Faculty of Economic
Sciences, University of Go¨ttingen. His research interests
include decision support systems, design science and IT
Governance, especially in the fields of E-Finance and
Electronic Markets. His research has appeared in outlets
such as Decision Support Systems and ICIS proceedings.
References
ABDELAAL A and ALI H (2007) A typology for community wireless
networks business models. In Proceedings of the 13th Americas
Conference on Information Systems (HOXMEIER JA and HAYNE S, Eds),
AIS, Keystone, CO.
ALDENDERFER MS and BLASHFIELD RK (1984)
Cluster
Analysis. Sage
Publications, Beverly Hills, CA.
ANDERBERG MR (1973) Cluster Analysis for Applications. Academic Press,
New York.
BAILEY KD (1984) A three-level measurement model. Quality and Quantity
18(3), 225–245.
BAILEY KD (1994) Typologies and Taxonomies – An Introduction to
Classification Techniques. Sage, Thousand Oaks, CA.
BAPNA R, GOES P, GUPTA A and YIWEI J (2004) User heterogeneity and its
impact on electronic auction market design: an empirical exploration.
MIS Quarterly 28(1), 21–43.
BOWKER GC and STAR SL (1999) Sorting Things Out: Classification and Its
Consequences. MIT Press, Cambridge, MA.
DOBSON S (2004) A taxonomy for thinking about location in pervasive
computing.
Technical
Report
TCD-CS-2004–05.
Department
of
Computer Science, Trinity College, Dublin.
DOGAC A, LALECI G, KABAK Y and CINGIL I (2002) Exploiting web service
semantics: taxonomies vs ontologies. Bulletin of the IEEE Computer
Society Technical Committee on Data Engineering.
DOMBROVIAK KM and RAMNATH R (2007) A taxonomy of mobile and
pervasive applications. In Proceedings of the 2007 ACM Symposium on
Applied Computing (CHO Y, WAINWRIGHT RL, HADDAD H, SHIN SY and KOO
YW, Eds), pp 1609–1615, ACM, Seoul.
DOTY DH and GLICK WH (1994) Typologies as a unique form of theory
building: toward improved understanding and modeling. Academy of
Management Review 19(2), 230–251.
DOTY DH, GLICK WH and HUBER GP (1993) Fit, equifinality, and
organizational effectiveness: a test of two configurational theories.
Academy of Management Journal 36(6), 1195–1250.
ELDREDGE N and CRACRAFT J (1980) Phylogenetic Patterns and the
Evolutionary Process. Columbia University Press, New York.
FIEDLER KD, GROVER V and TENG JTC (1996) An empirically derived
taxonomy of information technology structure and its relationship to
organizational structure. Journal of Management Information Systems
13(1), 9–34.
GEIGER
D,
SCHULZE
T,
SEEDORF
S,
NICKERSON
RC
and
SCHADER
M
(2011) Managing the crowd: towards a taxonomy of crowdsourcing
processes. In Proceedings of the 17th Americas Conference on Information
Systems (SAMBAMURTHY V and TANNIRU M, Eds), AIS, Detroit, MI.
GLASS
RL
and
VESSEY
I
(1995)
Contemporary
application-domain
taxonomies. IEEE Software 12(4), 63–76.
GOGUEN JA and LINDE C (1993) Techniques of requirements elicitation.
In
Proceedings
of
the
International
Symposium
on
Requirements
Engineering (FICKAS S and FINKELSTEIN A, Eds), pp 152–164, IEEE
Computer Society, San Diego, CA.
GREGOR S (2006) The nature of theory in information systems. MIS
Quarterly 30(3), 611–642.
GROVE A (2003) Taxonomy. Encyclopedia of Library and Information Science
pp 2770–2777, Marcel Dekker, New York.
GRUBER TR (1993) A translation approach to portable ontology specifica-
tions. Knowledge Acquisition 5(2), 199–220.
GRUNINGER M, BODENREIDER O, OLKEN F, OBRST L and YIM P (2008)
Ontology summit 2007 – ontology, taxonomy, folksonomy: under-
standing the distinctions. Applied Ontology 3(3), 191–200.
GUARINO N (1998) Formal ontology and information systems. In
Proceedings of FOIS ‘98 (GUARINO N, Ed), pp 3–15, IOS Press, Trento.
A method for taxonomy development
Robert C. Nickerson et al
355
European Journal of Information Systems

## Page 21

HEINONEN K and PURA M (2006) Developing a conceptual framework for
mobile services. In Proceedings of the Helsinki Mobility Roundtable
(JARVENPAA S, SAARINEN T and KRISTIINA V, Eds), Helsinki School of
Economics, Helsinki.
HEVNER AR and CHATTERJEE S (2010) Design Science Research in Information
Systems. Springer, New York.
HEVNER AR, MARCH ST, PARK J and RAM S (2004) Design science in
information systems research. MIS Quarterly 28(1), 75–105.
HIRSCHHEIM RA, KLEIN HK and LYYTINEN K (1995) Information Systems
Development and Data Modeling: Conceptual and Philosophical Founda-
tions. Cambridge University Press, Cambridge.
IIVARI J (2007) A paradigmatic analysis of information systems as a design
science. Scandinavian Journal of Information Systems 19(2), 39–64.
KEMPER H and WOLF E (2002) Iterative process models for mobile
application systems: a framework. In Proceedings of the 23rd Interna-
tional Conference on Information Systems (MIRALLES F and VALOR J, Eds),
pp 401–413, AIS, Barcelona.
KRUG S, CAMPIDELLI H and NICKERSON RC (2012) A preliminary taxonomy
for software failure impact: categorizing the impact on enterprises
when software fails. In Proceedings of the 18th Americas Conference on
Information Systems (Jessup L and Valacich J, Eds), Seattle, Washington.
LEEM CS, SUH HS and KIM DS (2004) A classification of mobile business
models and its applications. Industrial Management & Data Systems
104(1), 78–87.
LEHMANN H and LEHNER F (2002) Making sense of mobile applications – a
critical note to recent approaches to their taxonomy and classification.
In Proceedings of the 15th Bled eCommerce Conference (GRICAR J, Ed),
pp 493–507, AIS, Bled.
MARCH ST and SMITH GF (1995) Design and natural science research on
information technology. Decision Support Systems 15(4), 251–266.
MCKINNEY JC (1966) Constructive Typology and Social Theory. Appleton-
Centur-Crofts, New York.
MCKNIGHT DH and CHERVANY NL (2001) What trust means in e-commerce
customer relationships: an interdisciplinary conceptual typology.
International Journal of Electronic Commerce 6(2), 35–59.
MILLER GA (1956) The magic number seven, plus or minus two: some
limits on our capacity for processing information. Psychological Review
101(2), 343–352.
MILLER JG and ROTH AV (1994) A taxonomy of manufacturing strategies.
Management Science 40(3), 285–304.
NGAI EWT and GUNASEKARAN A (2007) A review for mobile commerce
research and applications. Decision Support Systems 43(1), 3–15.
NICKERSON R (1997) A taxonomy of collaborative applications. In
Proceedings of the 3rd Americas Conference on Information Systems
(GUPTA JND, Ed), pp 560–562, AIS, Indianapolis, IN.
NICKERSON R, MUNTERMANN J and VARSHNEY U (2010) Taxonomy
development
in
information
systems:
a
literature
survey
and
problem statement. In Proceedings of the 16th Americas Conference
on Information Systems (SANTANA M, LUFTMAN JN and VINZE AS, Eds),
AIS, Lima.
NICKERSON R, VARSHNEY U, MUNTERMANN J and ISAAC H (2007) Towards
a taxonomy of mobile applications. In Proceedings of the 13th
Americas Conference on Information Systems (HOXMEIER JA and HAYNE S,
Eds), AIS, Keystone, Co.
NICKERSON R, VARSHNEY U, MUNTERMANN J and ISAAC H (2009) Taxonomy
development in information systems: developing a taxonomy of
mobile applications. In Proceedings of the European Conference on
Information Systems (NEWELL A, WHITLEY EA, POULOUDI N, WAREHAM J and
MATHIASSEN L, Eds), AIS, Verona.
NYSVEEN H, PEDERSEN PE and THORBJøRNSEN H (2005) Intentions to use
mobile services: antecedents and cross-service comparisons. Journal of
the Academy of Marketing Science 33(3), 330–346.
PARSONS J and WAND Y (2008) Using cognitive principles to guide
classification in information systems modeling. MIS Quarterly 32(4),
839–868.
PINTO HS and MARTINS JP (2004) Ontologies: how can they be built?
Knowledge and Information Systems 6(4), 441–464.
SABHERWAL R and KING WR (1995) An empirical taxonomy of the decision-
making processes concerning strategic applications of information
systems. Journal of Management Information Systems 11(4), 177–214.
SCHWARZ A, MEHTA M, JOHNSON N and CHIN WW (2007) Understanding
frameworks and reviews: a commentary to assist us in moving our field
forward
by analyzing our past. The Database
for
Advances in
Information Systems 38(3), 29–50.
SIMON HA (1969) The Sciences of the Artificial. The MIT Press, Cambridge,
MA.
SOKAL RR and SNEATH PHA (1963) Principles of Numerical Taxonomy.
W.H. Freeman and Company, San Francisco, CA.
SOWA JF and ZACHMAN JA (1992) Extending and formalizing the
framework for information systems architecture. IBM Systems Journal
31(3), 590–616.
VARSHNEY U and VETTER R (2002) Mobile commerce: framework,
applications and networking support. Mobile Networks and Applications
7(3), 185–198.
WAND Y, MONARCHI DE, PARSONS J and WOO CC (1995) Theoretical
foundations for conceptual modeling in information systems develop-
ment. Decision Support Systems 15(4), 285–304.
WAND Y and WEBER R (2004) Reflection: ontology in information systems.
Journal of Database Management 15(2), iii–vi.
WEBER M (1949) The Methodology of the Social Sciences. Translated by
SHILS EA and FINCH HA. Free Press, Glencoe, IL.
WILLIAMS K, CHATTERJEE S and ROSSI M (2008) Design of emerging digital
services: a taxonomy. European Journal of Information Systems 17(5),
505–517.
Appendix
Papers surveyed
1. ABDELAAL
A
and
ALI
H
(2007)
A
typology
for
community wireless networks business models. In
Proceedings of the 13th Americas Conference on Informa-
tion Systems (HOXMEIER JA and HAYNE S, Eds), AIS,
Keystone, Co.
2. ALTER S (1977) A taxonomy of decision support
systems. Sloan Management Review 19(1), 39–56.
3. ANDERSON
GA
and
JENSEN
ED
(1975)
Computer
interconnection structures: taxonomy, characteris-
tics, and examples. ACM Computing Surveys 7(4),
197–213.
4.
ARRANGA
EC
(2000)
Cobol
tools:
Overview
and
taxonomy. IEEE Software 17(2), 59–61.
5.
BALL N, ADAMS C and XIA W (2004) IS/IT architecture:
an integrated view and typology. In Proceedings
of
the
10th
Americas
Conference
on
Information
Systems (BULLEN C and STOHR E, Eds), pp 3753–3754,
AIS, New York.
6.
BERANEK D and HORAN T (2006) Toward an empirical
user taxonomy for personal health records systems.
In Proceedings of the 12th Americas Conference on
Information Systems (RODRGUEZ-ABITIA, G and IGNACIO
AB, Eds), pp 2806–2810, AIS, Acapulco.
7.
BITTON D, DEWITT DJ, HSAIO DK and MENON J (1984)
A taxonomy of parallel sorting. ACM Computing
Surveys 16(3), 287–318.
8.
BLUM BI (1994) A taxonomy of software development
methods. Communications of the ACM 37(11), 82–94.
A method for taxonomy development
Robert C. Nickerson et al
356
European Journal of Information Systems

## Page 22

9. CARMEL E and EISENBERG J (2006) Narratives that
software nations tell themselves: an exploration and
taxonomy.
Communications
of
the
Association
for
Information Systems 17(1), 851–872.
10. CARR P and LU Y (2007) Information technology and
knowledge worker productivity: a taxonomy of
technology crowding. In Proceedings of the 13th
Americas Conference on Information Systems (HOXMEIER
JA and HAYNE S, Eds), AIS, Keystone, Co.
11. CASAVANT TL (1988) A taxonomy of scheduling in
general-purpose distributed computing systems. IEEE
Transactions on Software Engineering 14(2), 141–154.
12. CHANDRASEKARAN B (1983) Towards a taxonomy of
problem solving types. AI Magazine 4(1), 9–17.
13. CHIKOFSKY EJ and CROSS II JH (1990) Reverse en-
gineering and design recovery: a taxonomy. IEEE
Software 7(1), 13–17.
14. CHUANG S-L and CHIEN L-F (2003) Enriching Web
taxonomies through subject categorization of query
terms from search engine logs. Decision Support
Systems 35(1), 113–127.
15. CHUANG S and CHIEN L (2005) Taxonomy genera-
tion
for
text
segments:
a
practical
web-based
approach. ACM Transactions on Information Systems
23(4), 363–396.
16. COTTERMAN WW and KUMAR K (1989) User cube:
a taxonomy of end users. Communications of the
ACM 32(11), 1313–1320.
17. CRAINIC TG, TOULOUSE M and GENDREAU M (1997)
Towards a taxonomy of parallel tabu search heur-
istics. INFORMS Journal of Computing 9(1), 61–72.
18. DELGADO
N,
GATES
AQ
and
ROACH
S
(2004)
A
taxonomy and catalog of runtime software-fault
monitoring tools. IEEE Transactions on Software En-
gineering 30(12), 859–872.
19. DENNING DE and BRANSTAD D (1996) A taxonomy for
key escrow encryption systems. Communications of the
ACM 39(3), 34–40.
20. DUCASSE S and POLLET D (2009) Software architecture
reconstruction: a process-oriented taxonomy. IEEE
Transactions on Software Engineering 35(4), 573–591.
21. DURCIKOVA A and EVERARD A (2002) An employee
typology: a knowledge management perspective.
In Proceedings of the 8th Americas Conference on
Information Systems (BANKER RD, CHANG H and KAO
Y-C, Eds), pp 2042–2048, AIS, Dallas, Texas.
22. EARL M (2001) Knowledge management strategies:
toward a taxonomy. Journal of Management Informa-
tion Systems 18(1), 215–233.
23. FARBEY B, LAND F and TARGETT D (1995) A taxonomy
of information systems applications: the benefits
evaluation ladder. European Journal of Information
Systems 4(1), 41–50.
24. FIEDLER KD, GROVER V and TENG JTC (1996) An empi-
rically derived taxonomy of information techno-
logy structure and its relationship to organizational
structure. Journal of Management Information Systems
13(1), 9–34.
25. FILLEY
A
and
ALDAG
R
(1978)
Characteristics
and measurement of an organizational typology.
Academy of Management Journal 21(4), 578–591.
26. GILLENSON ML, SHERRELL DL and CHEN L (2000)
A taxonomy of web site traversal patterns and
structures. Communications of the Association for In-
formation Systems 3(1), Article 17.
27. GREGG DG and SCOTT JE (2008) A typology of
complaints about Ebay sellers. Communications of
the ACM 51(4), 69–74.
28. GUMM DC (2006) Distribution dimensions in soft-
ware development projects: a taxonomy. IEEE Soft-
ware 23(5), 45–51.
29. HAMBRICK D (1983) An empirical typology of mature
industrial-product environments. Academy of Mana-
gement Journal 26(2), 213–230.
30. HASAN H (2009) A taxonomy of modes of know-
ledge sharing between disparate group. In Proceed-
ings of the 13th Pacific Asia Conference on Informa-
tion Systems (BAPNA R and SAMBAMURTHY V, Eds), AIS,
Hyderabad.
31. IRANI
Z
and
LOVE
P
(2001)
The
propaga-
tion of technology management taxonomies for
evaluating investments in information systems.
Journal of Management Information Systems 17(3),
161–177.
32. KAFENTZIS K, APOSTOLOU D and MENTZAS G (2004)
Interorganizational
knowledge
management
sys-
tems: typology and cases. In Proceedings of the
13th European Conference on Information Systems (LEINO
T, SAARINEN T and KLEIN S), AIS, Turku.
33. KAYWORTH T, BROCATO L and WHITTEN D (2005)
What is a chief privacy officer? An analysis based
on Mintzberg’s taxonomy of managerial roles. Com-
munications of the Association for Information Systems
16(6), 110–126.
34. KEARNS GS (2005) An electronic commerce strategic
typology: insights from case studies. Information &
Management 42(7), 1023–1036.
35. LANDWEHR C, BULL A, MCDERMOTT J and CHOI W (1994)
A taxonomy of computer program security flaws.
ACM Computing Surveys 26(3), 211–254.
36. LARSEN K (2003) A taxonomy of antecedents of infor-
mation systems success: variable analysis studies.
Journal of Management Information Systems 20(2),
169–246.
37. LAUFER A (1968) A taxonomy of management theory:
a preliminary framework. Academy of Management
Journal 11(4), 435–442.
38. LEROUGE C and GJESTLAND C (2002) A typology of
data
warehouse
quality.
In
Proceedings
of
the
8th
Americas
Conference
on
Information
Systems
(BANKER RD, CHANG H and KAO Y-C, Eds), pp 34–37,
AIS, Dallas, Texas.
39. LIMONAD L and WAND Y (2009) A conceptual
model and typology for Information Systems
controls.
In
Proceedings
of
the
13th
Americas
Conference on Information Systems (NICKERSON RC
A method for taxonomy development
Robert C. Nickerson et al
357
European Journal of Information Systems

## Page 23

and SHARDA R, Eds), pp 1–9, AIS, San Francisco,
California.
40. LO´ PEZ TS, RANASINGHE DC, PATKAI B and MCFARLANE D
(2009)
Taxonomy,
technology
and
applications
of smart objects. Information Systems Frontiers 11(4),
1–20.
41. LU Y and CAMPBELL S (2007) Managing the dark side
of computer use at work: a typology of information
technology abuse and management strategy. In
Proceedings of the 13th Americas Conference on Informa-
tion Systems (HOXMEIER JA and HAYNE S, Eds), AIS,
Keystone, Co.
42. MCKNIGHT D and CHERVANY N (2001) What trust
means in E-commerce customer relationships: an
interdisciplinary conceptual taxonomy. International
Journal of Electronic Commerce 6(2), 35–59.
43. MCKNIGHT D, CHOUDHURY V and KACMAR C (2002)
Developing
and
validating
trust
measures
in
e-commerce: an integrative typology. Information
Systems Research 13(3), 334–359.
44. MERRITT S (1985) An inverted taxonomy of sorting
algorithms.
Communications
of
the
ACM
28(1),
96–99.
45. MESO P and MADEX G (2000) A complexity-based
taxonomy of systems development methodologies.
In Proceedings of the 6th Americas Conference on Informa-
tion Systems (CHUNG M, Ed), AIS, Long Beach, CA.
46. MILLER
J
and
ROTH
A
(1994)
A
taxonomy
of
manufacturing strategies. Management Science 40(3),
285–304.
47. MISTILIS N and DAMBRA J (2007) A taxonomy of
virtual information tasks and e-capability of visitor
information centres: an Australian case study. In
Proceedings of the 13th Americas Conference on Informa-
tion Systems (HOXMEIER JA and HAYNE S, Eds), AIS,
Keystone, Co.
48. MONARCHI D and PHUR G (1992) A research typology
for object-oriented analysis and design. Communica-
tions of the ACM 35(9), 35–47.
49. NARASIPURAM M (2006) Towards a taxonomy for
globally
distributed
work.
In
Proceedings
of
the
12th Americas Conference on Information Systems (RODR-
GUEZ-ABITIA, G and IGNACIO AB, Eds), pp 867–871, AIS,
Acapulco.
50. NICKERSON R (1997) A taxonomy of collaborative
applications.
In
Proceedings
of
the
3rd
Americas
Conference on Information Systems (GUPTA JND, Ed),
pp 560–562, AIS, Indianapolis.
51. NICKERSON R, VARSHNEY U, MUNTERMANN J and ISAAC H
(2007) Towards a taxonomy of mobile applications.
In Proceedings of the 13th Americas Conference on
Information Systems (HOXMEIER JA and HAYNE S, Eds),
AIS, Keystone, Co.
52. OLIVIER M and VON SOLMS S (1994) A taxonomy of
secure object-oriented databases. ACM Transactions on
Database Systems 19(1), 3–46.
53. PASWAN
A,
DSOUZA
D
and
ZOLFAGHARIAN
MA
(2009) Toward a contextually anchored service
innovation
typology.
Decision
Sciences
40(3),
513–540.
54. PEARSON J and SHIM J (1994) An empirical investi-
gation into decision support systems capabilities:
a proposed taxonomy. Information and Management
27(1), 45–57.
55. PLAISANT C, CARR D, and SHNEIDERMAN B (1995) Image-
browser taxonomy and guidelines for designers. IEEE
Software 12(2), 21–32.
56. PRUDEN HO (1973) The upward mobile, indifferent
and ambivalent typology of managers. Academy of
Management Journal 16(3), 454–464.
57. PUGLISI SJ, SMYTH WF and TURPIN AH (2007) A
taxonomy of suffix array construction algorithms.
ACM Computing Surveys 39(2), Article 4.
58. ROBINSON SL and BENNETT RJ (1995) A typology of
deviant workplace behaviors: a multidimensional
scaling study. Academy of Management Journal 38(2),
555–572.
59. SABHERWAL R and KING WR (1995) An empirical
taxonomy of the decision-making processes con-
cerning strategic applications of information sys-
tems. Journal of Management Information Systems 11(4),
177–214.
60. SABHERWAL
R
and
ROBEY
D
(1993)
An
empir-
ical
taxonomy
of
implementation
processes
based on sequences of events in information
systems development. Organization Science 4(4),
548–576.
61. SELMAN AL (1994) A taxonomy of complexity classes
of functions. Journal of Computer and System Sciences
48(2), 357–381.
62. SESTER A, EDER B and SCHEICHEL C (2006) Bless-
ing or curse? A taxonomy for virtual product
communities. In Proceedings of the 12th Americas
Conference on Information Systems (RODRGUEZ-ABITIA,
G and IGNACIO AB, Eds), pp 4495–4503, AIS,
Acapulco.
63. SHENHAR AJ and BONEN Z (1997) The new taxonomy
of systems: Toward an adaptive systems engineer-
ing framework. IEEE Transactions on Systems, Man,
and Cybernetics Part A: Systems and Humans 27(2),
137–145.
64. SON J and KIM SS (2008) Internet users’ informa-
tion
privacy-protective
responses:
a
taxonomy
and a nomological model. MIS Quarterly 32(3),
503–529.
65. SRINIVASAN V, DAVIDSON ES and TYSON GS (2004) A
prefetch taxonomy. IEEE Transactions on Computers
53(2), 126–140.
66. STEFANI RT (1999) A taxonomy of sports rating
systems.
IEEE
Transactions
on
Systems,
Man,
and
Cybernetics
Part
A:
Systems
and
Humans
29(1), 116–120.
67. TANGPONG C, MICHALISIN MD and MELCHER AJ (2008b)
Toward a typology of buyer-supplier relationships:
A study of the computer industry. Decision Sciences
39(3), 571–593.
A method for taxonomy development
Robert C. Nickerson et al
358
European Journal of Information Systems

## Page 24

68. VENUGOPAL S, BUYYA R and RAMAMOHANARAO K (2006)
A taxonomy of data grids for distributed data
sharing, management, and processing. ACM Comput-
ing Surveys 38(1), 1–53.
69. VEREECKE A, VAN DIERDONCK R and DE MEYER A (2006)
A
typology
of
plants
in
global
manufacturing
networks. Management Science 52(11), 1737–1750.
70. WANG H and WANG C (2003) Taxonomy of security
considerations in software quality. Communications of
the ACM 46(6), 75–78.
71. WILLIAMS JJ and RAMAPRASAD A (1996) A taxonomy
of critical success factors. European Journal of Informa-
tion Systems 5(4), 250–260.
72. WILLIAMS K, CHATTERJEE S and ROSSI M (2008) Design
of emerging digital services: A taxonomy. European
Journal of Information Systems 17(5), 505–517.
73. YOSHIOKA T, HERMAN G, YATES J and ORLIKOWSKI W
(2001) Genre taxonomy: A knowledge repository
of
communicative
actions.
ACM
Transactions
on
Information Systems 19(4), 431–456.
A method for taxonomy development
Robert C. Nickerson et al
359
European Journal of Information Systems
