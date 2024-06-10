from shiny import App, reactive, ui, render

timer = ui.HTML('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="timer " style="fill:currentColor;height:100%;" aria-hidden="true" role="img" ><path d="M8.5 5.6a.5.5 0 1 0-1 0v2.9h-3a.5.5 0 0 0 0 1H8a.5.5 0 0 0 .5-.5z"/><path d="M6.5 1A.5.5 0 0 1 7 .5h2a.5.5 0 0 1 0 1v.57c1.36.196 2.594.78 3.584 1.64l.012-.013.354-.354-.354-.353a.5.5 0 0 1 .707-.708l1.414 1.415a.5.5 0 1 1-.707.707l-.353-.354-.354.354-.013.012A7 7 0 1 1 7 2.071V1.5a.5.5 0 0 1-.5-.5M8 3a6 6 0 1 0 .001 12A6 6 0 0 0 8 3"/></svg>')

app_ui = ui.page_fluid(
    ui.panel_title("Survey Length Estimator"),
    ui.row(
        ui.column(8,
            ui.input_numeric("simple", "Number of simple questions (yes/no, or a simple scale)", value=0, width='800px'),
            ui.input_numeric("multi", "Total number of choices in multiple choice or rank questions", value=0, width='800px'),
            ui.input_numeric("short_ans", "Number of short response questions (1 Sentence expected)", value=0, width='800px'),
            ui.input_numeric("long_ans", "Number of long response questions (3-4 sentences expected)", value=0, width='800px'),
            ui.input_numeric("calculations", "Number of questions requiring minor calculations", value=0, width='800px'),
            ui.input_numeric("map", "Number of map or spatial response questions", value=0, width='800px'),
            ui.input_numeric("likert", """Total number of likert or "grid response" qestions""", value=0, width='800px'),
            ui.input_numeric("instructions", "Total number of sentances of instructions", value=0, width='800px')
        ),
        ui.column(4,
            ui.value_box(
                "Estimated Survey Length",
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
        minutes = int(time)
        seconds = int((time-minutes)*60)
        return f"{minutes} minute{plural(minutes)} and {seconds} second{plural(seconds)}"

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
