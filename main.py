
import sys

sys.path.insert(0, 'C:/Users/Admin/Desktop/py/notes')
import pynotes
import file_repository
import note_controller
import view



file_notes = file_repository.Repository("notes\data.csv");
controller = note_controller.Controller(file_notes);
view_notes = view.View(controller);
view_notes.run()


