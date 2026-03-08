"""
style_templates.py — DeDe Style Template Engine v1.0
=====================================================

Provides styled HTML templates for Canvas course pages.
Each style defines three page types: homepage, overview, assignment.

Styles:
  - azure_modern:  Navy (#173955) + light blue, clean grid, DesignPlus
  - blue_and_gold: Dark blue (#112d54) + gold (#f0c50c), layered cards, DesignPlus
  - none:          Plain HTML with minimal styling (Canvas default)

Usage:
  from style_templates import render_page
  html = render_page('azure_modern', 'homepage', data_dict)
"""


# ─────────────────────────────────────────────────────────────
#  STYLE REGISTRY
# ─────────────────────────────────────────────────────────────

STYLES = {
    'none': 'No Styling (Plain HTML)',
    'azure_modern': 'Azure Modern',
    'blue_and_gold': 'Blue & Gold',
}


def render_page(style, page_type, data):
    """
    Render a styled HTML page.

    Args:
        style: 'none', 'azure_modern', or 'blue_and_gold'
        page_type: 'homepage', 'overview', or 'assignment'
        data: dict with content fields (varies by page_type)

    Returns: complete HTML string for a Canvas wiki/assignment page
    """
    renderers = {
        'none': {
            'homepage':   _plain_homepage,
            'overview':   _plain_overview,
            'assignment': _plain_assignment,
        },
        'azure_modern': {
            'homepage':   _azure_homepage,
            'overview':   _azure_overview,
            'assignment': _azure_assignment,
        },
        'blue_and_gold': {
            'homepage':   _bluegold_homepage,
            'overview':   _bluegold_overview,
            'assignment': _bluegold_assignment,
        },
    }

    renderer = renderers.get(style, renderers['none'])
    func = renderer.get(page_type, renderer.get('overview'))
    return func(data)


def _esc(text):
    """HTML-escape text."""
    if not text:
        return ''
    return (str(text)
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def _render_list(items, tag='ul'):
    """Render a list of strings as HTML list items."""
    if not items:
        return ''
    li = ''.join(f'<li>{item}</li>' for item in items)
    return f'<{tag}>{li}</{tag}>'


# ─────────────────────────────────────────────────────────────
#  SHARED COMPONENTS
# ─────────────────────────────────────────────────────────────

def _azure_need_help():
    """Azure Modern "Need Help?" footer block."""
    return '''
<div class="dp-content-block" style="background-color: #173955; color: #ffffff;">
<h4 style="text-align: center;"><span style="font-size: 18pt;">Need Help?</span></h4>
<p style="text-align: center;"><span style="color: #ffffff;">Select the button that best meets the type of support you're looking for.</span></p>
<div class="dp-column-container container-fluid dp-padding-direction-tblr" style="padding-left: 150px; padding-right: 150px; color: #ffffff;">
<div class="row" style="color: #ffffff;">
<div class="col dp-margin-direction-all" style="background-color: #ffffff; color: #000000; margin: 5px;">
<p style="text-align: center;">Phone</p>
</div>
<div class="col dp-margin-direction-all" style="background-color: #ffffff; color: #000000; margin: 5px;">
<p style="text-align: center;">Chat</p>
</div>
<div class="col dp-margin-direction-all" style="background-color: #ffffff; color: #000000; margin: 5px;">
<p style="text-align: center;">Walk-in</p>
</div>
</div>
</div>
</div>'''


def _bluegold_need_help():
    """Blue & Gold "Need Help?" footer block."""
    return '''
<div class="dp-content-block kl_custom_block_4">
<div class="container-fluid">
<div class="row">
<div class="col-md" style="padding-bottom: 125px; border-color: #f0c50c; background-color: #f0c50c; color: #000000;">
<p>&nbsp;</p>
</div>
</div>
</div>
<div class="container-fluid">
<div class="row" style="background-color: #112d54; color: #ffffff;">
<div class="col-md" style="margin-right: 60px; margin-left: 60px; margin-top: -100px; color: #000000; background-color: #ffffff; padding-bottom: 10px; padding-top: 5px; border-radius: 5px;">
<div class="container-fluid">
<div class="row">
<div class="col-md" style="margin-top: 5px;">
<h2><span style="font-size: 18pt;"><strong>Need Help?</strong></span></h2>
<p><span style="font-size: 12pt;">Select the link that best meets the type of support you're looking for.</span></p>
</div>
<div class="col-md-7">
<div class="container-fluid">
<div class="row">
<div class="col-md" style="margin: 5px; background-color: #112d54; color: #ffffff; border-radius: 10px;">
<p style="text-align: center; padding: 15px;"><span style="color: #ffffff;">Phone</span></p>
</div>
<div class="col-md" style="margin: 5px; background-color: #112d54; color: #ffffff; border-radius: 10px;">
<p style="text-align: center; padding: 15px;"><span style="color: #ffffff;">Chat</span></p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="container-fluid">
<div class="row">
<div class="col-md" style="background-color: #112d54; color: #ffffff; padding-bottom: 0px;">
<p>&nbsp;</p>
</div>
</div>
</div>
</div>'''


# ─────────────────────────────────────────────────────────────
#  PLAIN / NO STYLING
# ─────────────────────────────────────────────────────────────

def _plain_homepage(data):
    """Minimal HTML homepage — no DesignPlus, just clean semantic HTML."""
    course_code = _esc(data.get('course_code', ''))
    course_title = _esc(data.get('course_title', ''))
    description = data.get('description', '')
    clos = data.get('clos', [])
    instructor = data.get('instructor_info', '')

    clo_html = ''
    if clos:
        clo_items = ''.join(
            f'<li><strong>{_esc(c.get("id", ""))}</strong> ({_esc(c.get("blooms", ""))}) — {_esc(c.get("text", ""))}</li>'
            for c in clos
        )
        clo_html = f'<h2>Course Learning Objectives</h2><ul>{clo_items}</ul>'

    return f'''<h1>Welcome to {course_code}: {course_title}</h1>
<h2>Course Description</h2>
<p>{description}</p>
{clo_html}
{f'<h2>Instructor Information</h2><p>{instructor}</p>' if instructor else ''}'''


def _plain_overview(data):
    """Minimal HTML module overview."""
    mod_title = _esc(data.get('module_title', ''))
    mod_num = data.get('module_number', '')
    overview = data.get('overview', '')
    mlos = data.get('mlos', [])
    materials = data.get('materials', [])
    assignments = data.get('assignments', [])
    discussion = data.get('discussion', '')

    mlo_html = ''
    if mlos:
        items = ''.join(
            f'<li><strong>{_esc(m.get("id", ""))}</strong> ({_esc(m.get("blooms", ""))}) — {_esc(m.get("text", ""))}</li>'
            for m in mlos
        )
        mlo_html = f'<h2>Module Learning Objectives</h2><p>By the end of this module, you will be able to:</p><ul>{items}</ul>'

    return f'''<h1>Module {mod_num}: {mod_title}</h1>
{f'<p>{overview}</p>' if overview else ''}
{mlo_html}
{f'<h2>Instructional Materials</h2>{_render_list(materials)}' if materials else ''}
{f'<h2>Assignments</h2>{_render_list(assignments)}' if assignments else ''}
{f'<h2>Discussion / Reflection</h2><p>{discussion}</p>' if discussion else ''}'''


def _plain_assignment(data):
    """Minimal HTML assignment page."""
    title = _esc(data.get('title', ''))
    instructions = data.get('instructions', '')
    points = data.get('points', '')
    due = data.get('due', '')
    sub_type = data.get('sub_type', '')
    purpose = data.get('purpose', '')
    rubric_html = data.get('rubric_html', '')

    return f'''<h1>{title}</h1>
<p><strong>Points:</strong> {_esc(points)} | <strong>Due:</strong> {_esc(due)} | <strong>Submission:</strong> {_esc(sub_type)}</p>
{f'<p><em>{_esc(purpose)}</em></p>' if purpose else ''}
<h2>Instructions</h2>
{instructions}
{f'<h2>Grading Rubric</h2>{rubric_html}' if rubric_html else ''}'''


# ─────────────────────────────────────────────────────────────
#  AZURE MODERN
# ─────────────────────────────────────────────────────────────

def _azure_clo_cards(clos):
    """Render CLOs as Azure Modern cards in a 2-column grid."""
    if not clos:
        return ''

    cards = []
    for c in clos:
        verb = _esc(c.get('blooms', 'Learn'))
        text = _esc(c.get('text', ''))
        cid = _esc(c.get('id', ''))
        cards.append(f'''
<div class="d-flex flex-row justify-content-center align-items-center text-center col">
<div class="dp-column-liner w-100 dp-padding-direction-tblr" style="background-color: #ffffff; color: #000000; border-radius: 10px; padding-left: 10px; padding-right: 10px;">
<h4><strong><span style="font-size: 14pt;">{verb}</span></strong></h4>
<p><span style="font-size: 10pt;">{text} ({cid})</span></p>
</div>
</div>''')

    # Arrange in rows of 2
    rows = []
    for i in range(0, len(cards), 2):
        pair = ''.join(cards[i:i+2])
        rows.append(f'''
<div class="dp-column-container container-fluid dp-padding-direction-tblr" style="padding-left: 30px; padding-right: 30px; padding-top: 15px;">
<div class="row">{pair}</div>
</div>''')

    return ''.join(rows)


def _azure_homepage(data):
    course_code = _esc(data.get('course_code', 'ABC1234'))
    course_title = _esc(data.get('course_title', 'Course Name'))
    description = data.get('description', '')
    clos = data.get('clos', [])

    clo_section = _azure_clo_cards(clos)

    return f'''<div id="dp-wrapper" class="dp-wrapper">
<div class="dp-content-block">
<div class="dp-column-container container-fluid">
<div class="row">
<div class="col-lg-6 col-md-6 col-sm-12 dp-padding-direction-tblr d-flex flex-row justify-content-start align-items-center text-start" style="padding-left: 50px; padding-right: 50px;">
<div class="dp-column-liner w-100">
<h2><span style="font-size: 18pt;">Welcome to&nbsp;</span></h2>
<h3><span style="font-size: 24pt;"><strong>{course_code}: {course_title}</strong></span></h3>
</div>
</div>
<div class="col-lg-6 col-md-6 col-sm-12 dp-padding-direction-tblr mx-auto d-block d-flex flex-row justify-content-center align-items-center text-center" style="padding-left: 50px; padding-right: 50px;">
<div class="dp-column-liner w-100">
<p><img class="object-fit-cover dp-ratio-4-5" style="height: auto;" src="https://files.ciditools.com/cidilabs/dp_icon_placeholder.jpg" alt="Course image placeholder" width="360" height="270" /></p>
</div>
</div>
</div>
</div>
</div>

<div class="dp-content-block dp-padding-direction-tblr" style="background-color: #173955; color: #ffffff; padding-top: 20px; padding-bottom: 40px; border-radius: 10px;">
<h3 class="dp-padding-direction-tblr" style="padding-left: 30px; padding-bottom: 20px;">Course Objectives</h3>
{clo_section}
</div>

<div class="dp-content-block dp-padding-direction-tblr dp-margin-direction-tblr" style="padding-top: 20px; background-color: #ffffff; color: #000000; margin-top: 30px;">
<h3 class="dp-padding-direction-tblr dp-margin-direction-tblr" style="padding-left: 30px; margin-top: 0px;">Course Description</h3>
<div class="dp-column-container container-fluid dp-padding-direction-tblr" style="padding-left: 30px; padding-right: 30px;">
<div class="row">
<div class="col-lg-12 col-md-12 col-sm-12 d-flex flex-row justify-content-start align-items-center text-start">
<div class="dp-column-liner w-100">
<p>{description}</p>
</div>
</div>
</div>
</div>
</div>

{_azure_need_help()}
</div>'''


def _azure_mlo_cards(mlos):
    """Render MLOs as Azure Modern cards in a row."""
    if not mlos:
        return ''

    cards = []
    for m in mlos:
        verb = _esc(m.get('blooms', 'Learn'))
        text = _esc(m.get('text', ''))
        cards.append(f'''
<div class="col dp-margin-direction-all dp-padding-direction-tblr" style="background-color: #173955; color: #ffffff; border-radius: 10px; margin: 5px; padding-bottom: 5px; padding-top: 5px;">
<p style="text-align: center;"><span style="font-size: 14pt;"><strong>{verb}</strong></span></p>
<p style="text-align: center;"><span>{text}</span></p>
</div>''')

    return f'''
<div class="dp-column-container container-fluid dp-padding-direction-tblr" style="padding-left: 25px; padding-right: 25px;">
<div class="row">{''.join(cards)}</div>
</div>'''


def _azure_overview(data):
    mod_num = data.get('module_number', '1')
    mod_title = _esc(data.get('module_title', 'Module Title'))
    overview = data.get('overview', '')
    mlos = data.get('mlos', [])
    materials = data.get('materials', [])
    assignments = data.get('assignments', [])

    mlo_section = _azure_mlo_cards(mlos)

    mat_items = ''.join(f'<li>{_esc(m)}</li>' for m in materials) if materials else '<li>See module content</li>'
    assign_items = ''.join(f'<li>{_esc(a)}</li>' for a in assignments) if assignments else ''

    return f'''<div id="dp-wrapper" class="dp-wrapper">
<div class="dp-content-block">
<div class="dp-bg dp-bg-image dp-padding-direction-tblr cp-bg-dp-primary text-light" style="background-position: center center; padding-bottom: 100px; padding-top: 100px; background-color: #173955; color: #ffffff;">
<h2 style="text-align: center;"><strong><span style="font-size: 52pt;">Module {mod_num}:&nbsp;</span></strong></h2>
<p style="text-align: center;"><span style="font-size: 36pt;">{mod_title}</span></p>
</div>
</div>

<div class="dp-content-block dp-padding-direction-all" style="padding: 20px;">
<h3 class="dp-padding-direction-tblr" style="padding-bottom: 15px; text-align: center;"><span style="font-size: 36pt;">Introduction</span></h3>
<p style="text-align: center;">{overview}</p>
</div>

<div class="dp-content-block dp-padding-direction-tblr" style="padding-bottom: 60px; padding-top: 20px;">
<h3 style="text-align: center;"><span style="font-size: 24pt;">Module Learning Objectives</span></h3>
{mlo_section}
</div>

<div class="dp-content-block dp-padding-direction-tblr" style="background-color: #173955; color: #ffffff; padding-top: 20px;">
<div class="dp-column-container container-fluid dp-padding-direction-all" style="padding: 25px;">
<div class="row">
<div class="col-lg-12 col-md-12 col-sm-12">
<h3 style="text-align: center;"><span style="font-size: 24pt;">Instructional Materials</span></h3>
<ul>{mat_items}</ul>
</div>
</div>
</div>
</div>

<div class="dp-content-block dp-padding-direction-tblr" style="padding-top: 20px;">
<div class="dp-column-container container-fluid">
<div class="row dp-padding-direction-tblr" style="padding-left: 30px; padding-right: 30px;">
<div class="col">
<h3 style="text-align: center;"><span style="font-size: 24pt;">Assessments &amp; Activities</span></h3>
<ul>{assign_items}</ul>
</div>
</div>
</div>
</div>

{_azure_need_help()}
</div>'''


def _azure_assignment(data):
    title = _esc(data.get('title', 'Assignment'))
    instructions = data.get('instructions', '')
    rubric_html = data.get('rubric_html', '')

    rubric_section = ''
    if rubric_html:
        rubric_section = f'''
<div class="dp-content-block dp-padding-direction-all" style="padding: 20px;">
<h3 class="dp-padding-direction-tblr" style="padding-bottom: 15px;"><span style="font-size: 24pt;">Grading Rubric</span></h3>
{rubric_html}
</div>'''

    return f'''<div id="dp-wrapper" class="dp-wrapper">
<div class="dp-content-block">
<div class="dp-bg dp-bg-image dp-padding-direction-tblr cp-bg-dp-primary text-light" style="background-position: center center; padding-bottom: 100px; padding-top: 100px; background-color: #173955; color: #ffffff;">
<h2 style="text-align: center;"><span style="font-size: 52pt;">{title}</span></h2>
</div>
</div>

<div class="dp-content-block dp-padding-direction-all" style="padding: 20px;">
<h3 class="dp-padding-direction-tblr" style="padding-bottom: 15px;"><span style="font-size: 36pt;">Instructions</span></h3>
<p>{instructions}</p>
</div>

{rubric_section}

{_azure_need_help()}
</div>'''


# ─────────────────────────────────────────────────────────────
#  BLUE & GOLD
# ─────────────────────────────────────────────────────────────

def _bluegold_homepage(data):
    course_code = _esc(data.get('course_code', 'ABC 1234'))
    course_title = _esc(data.get('course_title', 'Course Name'))
    description = data.get('description', '')
    instructor_name = _esc(data.get('instructor_name', 'Professor'))
    instructor_info = data.get('instructor_info', '')
    clos = data.get('clos', [])

    clo_html = ''
    if clos:
        items = ''.join(
            f'<li><strong>{_esc(c.get("id",""))}</strong> ({_esc(c.get("blooms",""))}) — {_esc(c.get("text",""))}</li>'
            for c in clos
        )
        clo_html = f'<h3 style="text-align: center;"><strong>Course Learning Objectives</strong></h3><ul>{items}</ul>'

    return f'''<div id="dp-wrapper" class="dp-wrapper">
<div class="dp-content-block">
<div class="dp-bg cp-bg-dp-primary dp-padding-direction-tblr dp-mask-drk-55 text-light dp-wcag-aa" style="background-color: #112d54; color: #ffffff; padding: 200px 50px 75px;">
<h2 style="text-align: center;"><strong><span style="font-size: 36pt;">Welcome to {course_code}</span></strong></h2>
<h3 style="text-align: center;"><strong>{course_title}</strong></h3>
<div class="dp-column-container container-fluid dp-margin-direction-tblr" style="margin-top: 60px;">
<div class="row">
<div class="col">
<div class="dp-bg cp-bg-warning dp-padding-direction-all" style="color: #000000; padding: 1px; border-radius: 25px; background-color: #ffcc00;">
<p style="text-align: center;">Start Here</p>
</div>
</div>
<div class="col" style="text-align: center;">
<div class="dp-bg cp-bg-warning dp-padding-direction-all" style="color: #000000; padding: 1px; border-radius: 25px; background-color: #ffcc00;">
<p style="color: #000000;">Syllabus</p>
</div>
</div>
</div>
</div>
</div>
</div>

<div class="dp-content-block dp-margin-direction-tblr" style="margin-top: 20px; padding: 30px;">
<div class="dp-card card" style="border-radius: 17px;">
<div class="card-body dp-padding-direction-all" style="background-color: #ffcc00; color: #000000; padding: 20px; border-radius: 10px;">
<h4 class="card-title"><span style="font-size: 24pt;">Course Overview</span></h4>
<p class="card-text">{description}</p>
{clo_html}
</div>
</div>
</div>

<div class="dp-content-block kl_custom_block_3 dp-margin-direction-tblr" style="padding-top: 20px; padding-bottom: 50px; background-color: #f5faff; color: #000000; margin-bottom: -15px;">
<h2 style="text-align: center; padding-top: 20px; padding-bottom: 20px; margin-top: 20px;"><span style="font-size: 36pt;"><strong>Meet Your Professor</strong></span></h2>
<div class="container-fluid">
<div class="row">
<div class="col-md">
<h3 style="text-align: center;"><strong>{instructor_name}</strong></h3>
<p>{instructor_info}</p>
</div>
</div>
</div>
</div>

{_bluegold_need_help()}
</div>'''


def _bluegold_mlo_cards(mlos):
    """Render MLOs as Blue & Gold cards in 2-column grid."""
    if not mlos:
        return ''

    cards = []
    for m in mlos:
        mid = _esc(m.get('id', ''))
        text = _esc(m.get('text', ''))
        maps = _esc(m.get('maps_to', ''))
        cards.append(f'''
<div class="col-md dp-shadow-r1 col" style="margin: 5px; background-color: #f6f5ff; color: #000000; border-radius: 10px;">
<h3 style="text-align: center;"><strong>{mid}</strong></h3>
<p>{text}{f" <strong>({maps})</strong>" if maps else ""}</p>
</div>''')

    # Arrange in rows of 2
    rows = []
    for i in range(0, len(cards), 2):
        pair = ''.join(cards[i:i+2])
        rows.append(f'''
<div class="container-fluid">
<div class="row dp-margin-direction-tblr" style="margin-right: 25px; margin-left: 25px;">
{pair}
</div>
</div>''')

    return ''.join(rows)


def _bluegold_overview(data):
    mod_num = data.get('module_number', '1')
    mod_title = _esc(data.get('module_title', 'Module Title'))
    overview = data.get('overview', '')
    mlos = data.get('mlos', [])
    materials = data.get('materials', [])
    assignments = data.get('assignments', [])

    mlo_section = _bluegold_mlo_cards(mlos)

    mat_items = ''.join(f'<li><p>{_esc(m)}</p></li>' for m in materials) if materials else ''
    assign_items = ''.join(f'<li>{_esc(a)}</li>' for a in assignments) if assignments else ''

    return f'''<div id="dp-wrapper" class="dp-wrapper">
<div class="dp-content-block">
<div class="dp-bg cp-bg-dp-primary dp-padding-direction-tblr" style="background-color: #112d54; color: #ffffff; padding: 80px 50px;">
<h2 style="text-align: center;"><span style="font-size: 36pt;"><strong>Module {mod_num}: {mod_title}</strong></span></h2>
</div>
</div>

<div class="dp-content-block kl_custom_block_2 dp-margin-direction-tblr">
<h2 style="padding-right: 10px; padding-left: 25px;"><span style="font-size: 24pt;"><strong>Introduction</strong></span></h2>
<p style="padding-right: 63px; padding-left: 25px;">{overview}</p>

{mlo_section}
</div>

<div class="dp-content-block kl_custom_block_3">
<div class="dp-bg dp-padding-direction-tblr cp-bg-dp-secondary" style="padding-top: 75px; background-color: #f0c50c; color: #000000;">
<p>&nbsp;</p>
</div>
</div>

<div class="dp-content-block kl_custom_block_4">
<h2 style="text-align: center; padding-top: 20px; padding-bottom: 20px;"><span style="font-size: 24pt;"><strong>Instructional Materials</strong></span></h2>
<div class="container-fluid">
<div class="row">
<div class="col-md">
<ul>{mat_items}</ul>
</div>
</div>
</div>
</div>

<div class="dp-content-block kl_custom_block_5"><hr />
<h2 style="text-align: center; padding-top: 20px; padding-bottom: 20px;"><span style="font-size: 24pt;"><strong>Assignments &amp; Activities</strong></span></h2>
<div class="container-fluid">
<div class="row">
<div class="col-md">
<ul style="list-style-type: disc;">{assign_items}</ul>
</div>
</div>
</div>
</div>

{_bluegold_need_help()}
</div>'''


def _bluegold_assignment(data):
    title = _esc(data.get('title', 'Assignment'))
    instructions = data.get('instructions', '')
    rubric_html = data.get('rubric_html', '')

    rubric_section = ''
    if rubric_html:
        rubric_section = f'''
<h3><strong>Grading Criteria</strong></h3>
{rubric_html}'''

    return f'''<div id="dp-wrapper" class="dp-wrapper">
<div class="dp-content-block dp-padding-direction-tblr" style="padding-left: 20px; padding-bottom: 16px;">
<div class="dp-bg cp-bg-dp-primary dp-padding-direction-tblr" style="padding-top: 30px;">
<div class="dp-column-container container-fluid">
<div class="row">
<div class="col-lg-9 col-md-9 col-sm-12 d-flex flex-row justify-content-start align-items-end text-start dp-margin-direction-tblr dp-padding-direction-all" style="background-color: #ffcc00; color: #000000; margin-bottom: -60px; padding: 20px; border-radius: 20px; margin-left: -20px;">
<div class="dp-column-liner w-100">
<h2><strong>{title}</strong></h2>
</div>
</div>
</div>
</div>
<p>&nbsp;</p>
</div>
</div>

<div class="dp-content-block kl_custom_block_0 dp-padding-direction-tblr" style="width: 100%; padding-top: 30px;">
<h3><strong>Instructions</strong></h3>
<p>{instructions}</p>

{rubric_section}

<h3><strong>How to Submit</strong></h3>
<p>Submit your work through the Canvas assignment submission link above.</p>
</div>

<div class="dp-content-block kl_custom_block_3">
<p>If you have any questions or concerns regarding the accessibility of this activity, please contact your instructor directly.</p>
</div>

{_bluegold_need_help()}
</div>'''
