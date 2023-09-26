
function run_sass()
{
  $.ajax({
    url: "/",
    type: 'post',
    data: {
      "sass_code": editor_sass.getValue(),
      "action": "run_sass"
    },
    success: function(responce){
      editor_css.setValue(responce, -1);
    },
    error: function(responce){
      console.log(2);
    }
  })
}