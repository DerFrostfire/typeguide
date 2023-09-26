function compile_ts()
{
  $.ajax({
    url: "/",
    type: 'post',
    data: {
      "ts_code": editor_ts.getValue(),
      "action": "run_sass"
    },
    success: function(responce){
      editor_js.setValue(responce, -1);
    },
    error: function(responce){
      console.log(2);
    }
  })
}