from shiny import App, reactive, ui, render

app_ui = ui.page_fluid(
    ui.panel_title("Counter Example"),
    ui.row(
        ui.column(6,
            ui.input_numeric("simple", "Number of Simple Questions", value=0),
            ui.input_numeric("multi", "Number of Multiple Selection or Rank Choices", value=0),
            ui.input_numeric("short_ans", "Number of Short Answer Questions (1 Sentence)", value=0),
            ui.input_numeric("long_ans", "Number of Long Response Questions (3-4 Sentences)", value=0),
            ui.input_numeric("map", "Number of Map or Spatial Responses", value=0),
            ui.input_numeric("instructions", "Number of Sentances of Instructions", value=1)
        ),
        ui.column(6,
            ui.value_box(
                "Survey Length (in Minutes)",
                value=ui.output_text("current_value"),

            )
        )
    )
)

def server(input, output, session):
    
    @render.text
    def current_value():
        simple_points = input.simple()
        multi_points = input.multi() / 2
        total = (simple_points + multi_points)/8
        return f"{round(total,1)} minutes total"

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()