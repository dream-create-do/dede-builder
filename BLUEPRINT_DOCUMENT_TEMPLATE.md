# MeMe Course Blueprint
> Produced by MeMe Coursewell | Blueprint Document v3.0
> This document is the direct input for DeDe, the Canvas course builder agent.
> **Do not alter section headers, field labels, or block delimiters.**
> DeDe reads this document programmatically — formatting must be exact.

---

## SECTION 1: COURSE IDENTITY

> DeDe uses Course Start Date + Class Meeting Days to resolve all relative dates
> (Week N, Day) into absolute calendar dates. Both fields are required.
> Course Start Date must be the first day of class (YYYY-MM-DD format).
> Class Meeting Days: comma-separated from Mon, Tue, Wed, Thu, Fri, Sat, Sun.

| Field | Value |
|-------|-------|
| Course Title | |
| Course Code | |
| Delivery Modality | |
| Institution | |
| Estimated Weeks | |
| Course Start Date | |
| Class Meeting Days | |
| Blueprint Version | |

---

## SECTION 2: COURSE-LEVEL LEARNING OBJECTIVES

> List all CLOs agreed upon during consultation. One per line, pipe-delimited.
> Every CLO must use a measurable Bloom's action verb.
> Every CLO must be assessed by at least one assignment in Section 6.
> Do NOT use unmeasurable verbs: understand, know, learn, appreciate, be aware of.

CLO-1 | Bloom's Level | Objective statement
CLO-2 | Bloom's Level | Objective statement

> FORMAT EXAMPLE (do not include this in the final Blueprint):
> CLO-1 | Analyze | Students will analyze the ethical implications of emerging AI technologies across healthcare, law, and education.
> CLO-2 | Apply | Students will apply psychological research methods to design a simple observational study.
> CLO-3 | Evaluate | Students will evaluate competing theoretical frameworks using evidence from primary sources.

---

## SECTION 3: COURSE SCHEDULE

> The authoritative week-by-week calendar for the course.
> Every module and every assignment must appear in this schedule.
> Week numbers must match the Module and Assignment blocks in Sections 5 and 6.
> Due items: list assignment names only — full details go in Section 6.

| Week | Topic / Focus | Module | Due This Week | Notes |
|------|--------------|--------|---------------|-------|
| 1 | | | | |

---

## SECTION 4: GRADING STRUCTURE

> DeDe uses this to build Canvas assignment groups with correct weights.
> Weights MUST sum to exactly 100. DeDe will reject any Blueprint where they do not.
> Drop Lowest N: enter 0 if not applicable.

| Group Name | Weight (%) | Drop Lowest N | Notes |
|------------|-----------|---------------|-------|
| | | 0 | |

---

## SECTION 5: MODULE BLUEPRINTS

> One block per module. Repeat the full block structure for every module.
> Use the exact delimiter: ### MODULE: N — Title
> The module number and em dash (—) before the title are required.
> Write "None" for any field that does not apply — do not leave fields blank.
>
> MLO format: MLO-N.M | Bloom's Level | Objective statement | CLO-N
>   where N = module number, M = objective number within that module
>   The final field (CLO-N) is REQUIRED — it specifies alignment.
>
> Availability dates use relative format: Week N, Day
>   DeDe resolves these to absolute dates at build time.

---

### MODULE: 1 — Module Title Here

**Availability:**
- Opens: Week 1, Mon
- Closes: Week 2, Sun

**Overview Text:**
Write the module introduction that students will see. This should explain what the module covers, why it matters, and what students will do. Write in complete sentences.

**Module Learning Objectives:**
MLO-1.1 | Bloom's Level | Objective statement | CLO-1
MLO-1.2 | Bloom's Level | Objective statement | CLO-2

**Assignments in This Module:**
> List assignment names only, one per line. Full details go in Section 6.
- Assignment Name Here

**Instructional Materials:**
> Title and type. Type options: Video | Reading | Podcast | Webpage | Tool | Slide Deck
- Material Title (Type)

**Discussion / Reflection Prompt:**
Write the discussion or reflection prompt text. If this module has no discussion, write "None".

**Notes for DeDe:**
Any special build instructions for this module. Write "None" if not applicable.

---

## SECTION 6: ASSIGNMENT BLUEPRINTS

> One block per assignment. Use the exact delimiter: ### ASSIGNMENT: Title
> The title after the colon becomes the assignment name in Canvas.
> Be thorough — this becomes the actual assignment page students see.
> Every assignment must map to at least one MLO and one CLO.
>
> All dates use relative format: Week N, Day
> Submission Type options: Text Entry | File Upload | External URL | Media Recording | No Submission
> Fink's Category options: Foundational Knowledge | Application | Integration | Human Dimension | Caring | Learning How to Learn
>
> Rubric: Use a markdown table with the columns shown below.
>   Point values per criterion should sum to Points Possible.
>   Write "None" if this assignment has no rubric (e.g., auto-graded quiz).

---

### ASSIGNMENT: Assignment Title Here

**Belongs To Module:** 1
**Assignment Group:** Group Name from Section 4
**Points Possible:** 100
**Due:** Week 2, Fri
**Available From:** Week 1, Mon
**Until:** Week 3, Sun
**Submission Type:** File Upload

**Purpose Statement:**
One to two sentences explaining why this assignment matters for student learning. Students see this.

**Instructions:**
Write the full assignment instructions that students will see. Include what they need to do, any formatting requirements, and how to submit. Write in complete, student-facing language.

**Rubric:**

| Criterion | Excellent | Satisfactory | Needs Improvement | Points |
|-----------|-----------|--------------|-------------------|--------|
| Criterion name | Description of excellent work | Description of satisfactory work | Description of work needing improvement | 25 |

**Maps to CLOs:** CLO-1, CLO-2
**Maps to MLOs:** MLO-1.1, MLO-1.2
**Fink's Category:** Application

**Academic Integrity Notes:**
Any design decisions made to promote academic integrity. Write "None" if not applicable.

---

## SECTION 7: COURSE POLICIES & SYLLABUS CONTENT

> This content becomes the Canvas syllabus page and policy pages.
> Write in complete sentences — this is student-facing content.
> Every field must have real content or "None". No placeholders.
> These fields directly support QM Standards 1.3, 1.4, 5.3, 7.1, 7.2, 7.3.

**Course Description:**
Write the catalog-style course description. Include the course's purpose within the program or discipline.

**Instructor Information:**
Name, title, email, office hours or availability window, preferred contact method, expected response time for emails and discussion posts.

**Required Materials:**
Textbooks (with ISBN), software, hardware, access codes, or other required purchases. Write "None" if no purchases are required.

**Attendance & Participation Policy:**
What does "attendance" mean in this course? How is participation measured? What are the consequences of non-participation?

**Late Work Policy:**
Is late work accepted? For how long? Is there a penalty? Are extensions available? Under what circumstances?

**Academic Integrity Policy:**
Expectations for original work, citation requirements, collaboration guidelines, AI tool policy, consequences for violations. Reference the institutional policy.

**Accessibility Statement:**
Link to institutional disability services, how to request accommodations, commitment to accessible design. Must include specific contact information — not just a generic statement.

**Additional Policies:**
Any course-specific policies not covered above (e.g., recording policy, social media policy, field trip requirements). Write "None" if not applicable.

---

## SECTION 8: TECHNOLOGY & TOOLS

> List every external tool used in the course beyond Canvas native features.
> Canvas-native tools (Discussions, Quizzes, Assignments, SpeedGrader) do not need listing.
> DeDe uses this to create LTI placeholder links and tool reference pages.

| Tool Name | Purpose | Required or Optional | Notes |
|-----------|---------|----------------------|-------|
| | | | |

---

## SECTION 9: BLUEPRINT CHANGE LOG

> MeMe completes this section at the end of consultation.
> This is a record for the instructor and ID — not instructions for DeDe.
> Transfer every Decision Log Entry from the consultation into this section.
> Be specific. Vague entries like "improved objectives" are not useful.

**Summary of Changes:**
Brief paragraph describing the overall scope of changes made during consultation.

**Decision Log:**
> Paste every Decision Log Entry from the consultation here, in order.

```
DECISION LOG ENTRY
Standard: 
Issue: 
Resolution: 
Blueprint impact: 
```

**Instructor Deferrals:**
> Record any items the instructor chose not to address, with their rationale.
> This is important for future QM review — it shows the decision was intentional.
- Standard X.X — Deferred. Rationale: [instructor's reason]

**QM Standards Addressed:**
> List each standard that improved as a result of consultation.
- Standard X.X — [What changed]

**UDL Improvements Made:**
> List UDL-related changes. Write "None" if no UDL changes were made.
- [Change description]

**Fink's Framework Additions:**
> List any assignments enhanced with Fink's categories. Write "None" if not applicable.
- [Change description]

---

## SECTION 10: AGENT BUILD INSTRUCTIONS

> Direct instructions from MeMe to DeDe.
> DeDe reads this section to determine how to handle the build.
> Be explicit — DeDe follows these literally.

**Build Mode:** FULL BUILD
> Options:
> FULL BUILD — build the entire course from scratch using this Blueprint
> UPDATE — modify an existing IMSCC file using this Blueprint as a patch

**Preserve From Original:**
> For UPDATE mode only. List elements DeDe should leave exactly as-is.
> Write "None" for FULL BUILD.
None

**Delete From Original:**
> For UPDATE mode only. List elements DeDe should remove entirely.
> Write "None" for FULL BUILD.
None

**Special Build Notes:**
> Any instructions that do not fit elsewhere. Write "None" if not applicable.
None

---

*MeMe Course Blueprint v3.0 — Handoff to DeDe*
*Generated by the CeCe / MeMe / DeDe Instructional Design Agent Suite*
