import os, json

import sublime
import sublime_plugin


class LoadListener(sublime_plugin.EventListener):
  def on_load(self, view):
    counter_path = os.path.expanduser('~/sublime_counter.txt')
    opened_path = view.file_name()
    path_to_count = {}
    if os.path.exists(counter_path):
      with open(counter_path) as f:
        json_text = f.read()
      path_to_count = json.loads(json_text)
    path_to_count.setdefault(opened_path, 0)
    path_to_count[opened_path] += 1
    json_text = json.dumps(path_to_count, indent=2)
    with open(counter_path, 'w') as f:
      f.write(json_text)
