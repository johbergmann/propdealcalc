##written by Johanna Bergmann

from shiny import App, render, ui


app_ui = ui.page_fluid(
    ui.h2("Property deal calculator"),
    # ui.input_slider("pp", "Purchase price", 0, 1000000, 10),
    ui.input_numeric("pp", "Property price", value=80),
    ui.input_numeric("mv", "Market value", value=100),
    ui.h4("Deal breakdown"),
    ui.output_text("pp_txt"),
    ui.output_text("mv_txt"),
    ui.output_text("bmv_txt")
    

)



def server(input, output, session):
    @output
    @render.text
    def pp_txt():
        
        if input.pp() is None:
           return "Purchase price is missing" 
        else:
            return f"Purchase price: {input.pp()} GBP" 
    
    @output
    @render.text
    def mv_txt():
        
        if input.mv() is None:
           return "Market value is missing" 
        else:
            return f"Market value: {input.mv()} GBP" 
    
    @output
    @render.text
    def bmv_txt():
        if input.pp() is None:
           
            return "BMV cannot be computed due to missing value(s)" 
        
        else: 
            BMV=round((1 - input.pp() / input.mv()) * 100, 2)
            return f"BMV: {BMV}%"  


app = App(app_ui, server)
