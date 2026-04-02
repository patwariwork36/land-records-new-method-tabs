import sys

with open('temp_script.js', 'r') as f:
    temp_lines = f.readlines()

replace_content = temp_lines[22:181] # lines 23-181

with open('index.html', 'r') as f:
    index_lines = f.readlines()

# find exact range to replace.
# in index.html:
# line 841:         // ══════════════════════════════════════════════════════════════
# line 842:         // ── नई Multi-Tab Google Sheet Config ───────────────────────
# line 1212:             }
# line 1213:         }

start_idx = 840
end_idx = 1213

new_index_lines = index_lines[:start_idx] + replace_content + index_lines[end_idx:]

with open('index.html', 'w') as f:
    f.writelines(new_index_lines)

print("index.html fixed.")
