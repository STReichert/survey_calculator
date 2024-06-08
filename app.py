from shiny import App, reactive, ui, render

timer = ui.HTML(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="c0c0c0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-timer"><line x1="10" x2="14" y1="2" y2="2"/><line x1="12" x2="15" y1="14" y2="11"/><circle cx="12" cy="14" r="8"/></svg>'
)

app_ui = ui.page_fluid(
    ui.panel_title("Counter Example"),
    ui.row(
        ui.column(6,
            ui.input_numeric("simple", "Number of simple questions (yes/no, or a simple scale)", value=0),
            ui.input_numeric("multi", "Total number of choices in multiple choice or rank questions", value=0),
            ui.input_numeric("short_ans", "Number of short response questions (1 Sentence expected)", value=0),
            ui.input_numeric("long_ans", "Number of long respponse questions (3-4 sentences expected)", value=0),
            ui.input_numeric("calculations", "Number of questions requiring minor calculations", value=0),
            ui.input_numeric("map", "Number of map or spatial response questions", value=0),
            i.input_numeric("likert", """Total number of likert or "grid response" qestions""", value=0),
            ui.input_numeric("instructions", "Total Number of Sentances of Instructions", value=1)
        ),
        ui.column(6,
            ui.value_box(
                "Survey Length",
                value=ui.output_text("current_value"),
                showcase=timer,
                theme="bg-gradient-blue-purple"
            )
        )
    )
)

def handle_none(value):
    """Return 0 if the value is None, otherwise return the value."""
    return 0 if value is None else value

def plural(value):
    """return 's' ending for plurals if needed"""
    return "" if value == 1 else "s"

def server(input, output, session):
    
    @render.text
    def current_value():
        simple_points = handle_none(input.simple())
        multi_points = handle_none(input.multi()) / 2
        short_points = handle_none(input.short_ans())*3
        long_points = handle_none(input.long_ans())*10
        map_points = handle_none(input.map())*4
        calc_points = handle_none(input.calculations())*2
        likert_points = handle_none(input.likert())
        instruction_points = handle_none(input.instructions())/3
        total = sum([simple_points, multi_points, short_points, long_points, map_points, calc_points, likert_points, instruction_points])
        time = total/8
        mintues = int(time)
        seconds = int((time-minutes)*60)
        return f"{minutes} minute{plural(minutes)} and {seconds} second{plural(seconds)}"

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
