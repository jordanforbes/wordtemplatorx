import dearpygui.dearpygui as dpg
# this is just a placeholder

def gui():
  def save_callback():
      print("Save Clicked")

  dpg.create_context()
  dpg.create_viewport()
  dpg.setup_dearpygui()
  # dpg.set_main_window_size(800, 600)

  with dpg.window(label="Example Window", tag="Primary Window"):
      dpg.add_text("fooo")
      dpg.add_button(label="Save", callback=save_callback)
      dpg.add_input_text(label="string")
      dpg.add_slider_float(label="float")

  # dpg.set_viewport(0, 0, 800, 600)
  dpg.create_viewport(title='Custom Title', width=600, height=200)
  dpg.show_viewport()
  dpg.set_primary_window("Primary Window", True)
  dpg.start_dearpygui()
  dpg.destroy_context()
