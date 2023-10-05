##written by Johanna Bergmann

from shiny import App, render, ui


app_ui = ui.page_fluid(
    
    {"style": "background-color: rgba(0, 128, 255, 0.1)"},
    ui.tags.style(
        """
        body {
            font-family: Arial
            }
        """
    ),
    
    # ui.panel_title("A basic absolute panel example", "Demo"),
    ui.panel_absolute(
        
        ui.panel_well(
        #     "Drag me around!", ui.input_slider("n", "N", min=0, max=100, value=20)
        # ),
        
        ui.h2("Property deal calculator"),
        # ui.input_slider("pp", "Purchase price", 0, 1000000, 10),
        ui.input_numeric("pp", "Property price", value=80000),
        ui.input_numeric("mv", "Market value", value=100000),
        ui.h4("Deal breakdown"),
        ui.output_text("pp_txt"),
        ui.output_text("mv_txt"),
        ui.output_text("bmv_txt"),
        
        draggable=True,
        width="300px",
        right="50px",
        top="50%",
            )
        )
    

)



def server(input, output, session):
    @output
    @render.text
    def pp_txt():
        
        if input.pp() is None:
           return "Purchase price is missing" 
        else:
            return f"Purchase price: {input.pp(): ,} GBP" 
    
    @output
    @render.text
    def mv_txt():
        
        if input.mv() is None:
           return "Market value is missing" 
        else:
            return f"Market value: {input.mv(): ,} GBP" 
    
    @output
    @render.text
    def bmv_txt():
        if input.pp() is None:
           
            return "BMV cannot be computed due to missing value(s)" 
        
        else: 
            BMV=round((1 - input.pp() / input.mv()) * 100, 2)
            # BMV = ui.tags(str(tmp), style="color: red;")
            return f"BMV: {BMV}%"  


app = App(app_ui, server)
