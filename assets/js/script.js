document.getElementById("button_check").addEventListener("click", function(){
  var check_text = document.getElementById("textarea1").value;
  var data = {
      text: check_text
  };
  var json = JSON.stringify(data);
  const Http = new XMLHttpRequest()
  const url='/check'
  // Http.open("POST", url)
  Http.open("POST", url)
  Http.send(json)
  Http.onreadystatechange=(e)=>{
      if(Http.readyState == 4 && Http.status == 200){
          resp = JSON.parse(Http.responseText)
          if(resp.message == "OK"){
              document.cookie = "session=" + resp.session_id.toString() + ";";
              window.location = "";
          }
          else{
              console.log(resp.message);
          }
      }
  }

})

document.getElementById("button_update").addEventListener("click", function(){
  var check_text = document.getElementById("textarea2").value;
  var data = {
      text: check_text
  };
  var json = JSON.stringify(data);
  const Http = new XMLHttpRequest()
  const url='/update'
  // Http.open("POST", url)
  Http.open("POST", url)
  Http.send(json)
  Http.onreadystatechange=(e)=>{
      if(Http.readyState == 4 && Http.status == 200){
          resp = JSON.parse(Http.responseText)
          if(resp.message == "OK"){
              document.cookie = "session=" + resp.session_id.toString() + ";";
              window.location = "";
          }
          else{
              console.log(resp.message);
          }
      }
  }

})