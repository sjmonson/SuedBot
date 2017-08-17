function add_load_listener(fn)
{
if (typeof window.addEventListener != 'undefined')
{
window.addEventListener('load', fn, false);
}
else if (typeof document.addEventListener != 'undefined')
{
document.addEventListener('load', fn, false);
}
else if (typeof window.attachEvent != 'undefined')
{
window.attachEvent('onload', fn);
}
else
{
var oldfn = window.onload;
if (typeof window.onload != 'function')
{
window.onload = fn;
}
else
{
window.onload = function()
{
oldfn();
fn();
};
}
}
}
function attach_event_listener(target, event_type, function_reference, capture)
{
if (typeof target.addEventListener != 'undefined')
{
target.addEventListener (event_type, function_reference, capture);
}
else if (typeof target.attachEvent != 'undefined')
{
target.attachEvent ('on' + event_type, function_reference);
}
else
{
event_type = 'on' + event_type;
if (typeof target[event_type] == 'function')
{
var old_listener = target[event_type];
target[event_type] = function()
{
old_listener();
return function_reference();
};
}
else
{
target[event_type] = function_reference;
}
}
}