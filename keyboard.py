import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import bpy

from animatelib import animate_assemble, seconds_to_frames

STAGGER_SECONDS = 0.02
DISTANCE = 2.0
LENGTH = 1.0

esc = bpy.data.objects["esc"]
tilde = bpy.data.objects["tilde"]
tab = bpy.data.objects["tab"]
capslock = bpy.data.objects["capslock"]
lshift = bpy.data.objects["lshift"]
lctrl = bpy.data.objects["lctrl"]
f1 = bpy.data.objects["f1"]
key_1 = bpy.data.objects["1"]
q = bpy.data.objects["q"]
a = bpy.data.objects["a"]
z = bpy.data.objects["z"]
windows = bpy.data.objects["windows"]
f2 = bpy.data.objects["f2"]
key_2 = bpy.data.objects["2"]
w = bpy.data.objects["w"]
s = bpy.data.objects["s"]
x = bpy.data.objects["x"]
lalt = bpy.data.objects["lalt"]
f3 = bpy.data.objects["f3"]
key_3 = bpy.data.objects["3"]
e = bpy.data.objects["e"]
d = bpy.data.objects["d"]
c = bpy.data.objects["c"]
f4 = bpy.data.objects["f4"]
key_4 = bpy.data.objects["4"]
r = bpy.data.objects["r"]
f = bpy.data.objects["f"]
v = bpy.data.objects["v"]
space = bpy.data.objects["space"]
f5 = bpy.data.objects["f5"]
key_5 = bpy.data.objects["5"]
t = bpy.data.objects["t"]
g = bpy.data.objects["g"]
b = bpy.data.objects["b"]
f6 = bpy.data.objects["f6"]
key_6 = bpy.data.objects["6"]
y = bpy.data.objects["y"]
h = bpy.data.objects["h"]
n = bpy.data.objects["n"]
f7 = bpy.data.objects["f7"]
key_7 = bpy.data.objects["7"]
u = bpy.data.objects["u"]
j = bpy.data.objects["j"]
m = bpy.data.objects["m"]
f8 = bpy.data.objects["f8"]
key_8 = bpy.data.objects["8"]
i = bpy.data.objects["i"]
k = bpy.data.objects["k"]
left_angle_bracket = bpy.data.objects["left_angle_bracket"]
ralt = bpy.data.objects["ralt"]
f9 = bpy.data.objects["f9"]
key_9 = bpy.data.objects["9"]
o = bpy.data.objects["o"]
key_l = bpy.data.objects["l"]
right_angle_bracket = bpy.data.objects["right_angle_bracket"]
rwindows = bpy.data.objects["rwindows"]
f10 = bpy.data.objects["f10"]
key_0 = bpy.data.objects["0"]
p = bpy.data.objects["p"]
colon = bpy.data.objects["colon"]
question_mark = bpy.data.objects["question_mark"]
rfn = bpy.data.objects["rfn"]
f11 = bpy.data.objects["f11"]
minus = bpy.data.objects["minus"]
open_square_bracket = bpy.data.objects["open_square_bracket"]
quote = bpy.data.objects["quote"]
rshift = bpy.data.objects["rshift"]
rctrl = bpy.data.objects["rctrl"]
f12 = bpy.data.objects["f12"]
plus = bpy.data.objects["plus"]
close_square_bracket = bpy.data.objects["close_square_bracket"]
enter = bpy.data.objects["enter"]
print_screen = bpy.data.objects["print_screen"]
backspace = bpy.data.objects["backspace"]
pipe = bpy.data.objects["pipe"]
up = bpy.data.objects["up"]
scroll_lock = bpy.data.objects["scroll_lock"]
insert = bpy.data.objects["insert"]
delete = bpy.data.objects["delete"]
left = bpy.data.objects["left"]
pause = bpy.data.objects["pause"]
home = bpy.data.objects["home"]
end = bpy.data.objects["end"]
down = bpy.data.objects["down"]
page_up = bpy.data.objects["page_up"]
page_down = bpy.data.objects["page_down"]
right = bpy.data.objects["right"]
num_lock = bpy.data.objects["num_lock"]
num7 = bpy.data.objects["num7"]
num4 = bpy.data.objects["num4"]
num1 = bpy.data.objects["num1"]
num_0 = bpy.data.objects["num_0"]
forward_slash = bpy.data.objects["forward_slash"]
num8 = bpy.data.objects["num8"]
num5 = bpy.data.objects["num5"]
num2 = bpy.data.objects["num2"]
asterisk = bpy.data.objects["asterisk"]
num9 = bpy.data.objects["num9"]
num6 = bpy.data.objects["num6"]
num3 = bpy.data.objects["num3"]
num_decimal = bpy.data.objects["num_decimal"]
num_minus = bpy.data.objects["num_minus"]
num_plus = bpy.data.objects["num_plus"]
tall_enter = bpy.data.objects["tall_enter"]

keys = [
    esc,
    tilde,
    tab,
    capslock,
    lshift,
    lctrl,
    f1,
    key_1,
    q,
    a,
    z,
    windows,
    f2,
    key_2,
    w,
    s,
    x,
    lalt,
    f3,
    key_3,
    e,
    d,
    c,
    f4,
    key_4,
    r,
    f,
    v,
    space,
    f5,
    key_5,
    t,
    g,
    b,
    f6,
    key_6,
    y,
    h,
    n,
    f7,
    key_7,
    u,
    j,
    m,
    f8,
    key_8,
    i,
    k,
    left_angle_bracket,
    ralt,
    f9,
    key_9,
    o,
    key_l,
    right_angle_bracket,
    rwindows,
    f10,
    key_0,
    p,
    colon,
    question_mark,
    rfn,
    f11,
    minus,
    open_square_bracket,
    quote,
    rshift,
    rctrl,
    f12,
    plus,
    close_square_bracket,
    enter,
    print_screen,
    backspace,
    pipe,
    up,
    scroll_lock,
    insert,
    delete,
    left,
    pause,
    home,
    end,
    down,
    page_up,
    page_down,
    right,
    num_lock,
    num7,
    num4,
    num1,
    num_0,
    forward_slash,
    num8,
    num5,
    num2,
    asterisk,
    num9,
    num6,
    num3,
    num_decimal,
    num_minus,
    num_plus,
    tall_enter,
]

stagger_frames = seconds_to_frames(STAGGER_SECONDS)
for i, key in enumerate(keys):
    end_frame = (i + 1) * stagger_frames + seconds_to_frames(LENGTH)
    animate_assemble(key, end_frame, LENGTH, DISTANCE)

bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
