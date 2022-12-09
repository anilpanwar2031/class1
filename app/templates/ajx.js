<script>
$("#qsearch").keyup(function()
{
  output="";
  let s = $("#qsearch").val();
  console.log(s);
  let csr = $("input[name=csrfmiddlewaretoken]").val();
  mydata = {search : s, csrfmiddlewaretoken: csr};
  $.ajax(
  {
    url: "{% url 'qsearch' %}",
    method: "POST",
    data: mydata,
    dataType: "json",
    success: function(data)
    {
        console.log("in ajax success");
        console.log(data);
        for (let i = 0; i < data.length; i++)
        {
         console.log(data[i]["name"]);
         output += "<tr><td><a href='{% url 'quotation'" + data[i]["id"] + "%}'>" + data[i]["quot_no"] + "</a></td><td>" + data[i]["name"] +
                       "</td><td>" + data[i]["quot_status"] + "</td><td>" + data[i]["market_seg"] +
                       "</td><td>" + data[i]["created_at"] + "</td><td>" + data[i]["created_by"] +
                      "</td><td class='fw-bold'>R 320</td></tr>";
        }

        $("#qtbody").html(output);

    }
  })
});


$("#psearch").keyup(function()
{
  output="";
  pdsearch="";
  let s = $("#psearch").val();
  console.log(s);
  let csr = $("input[name=csrfmiddlewaretoken]").val();
  mydata = {search : s, csrfmiddlewaretoken: csr};
  $.ajax(
  {
    url: "{% url 'psearch' %}",
    method: "POST",
    data: mydata,
    dataType: "json",
    success: function(data)
    {
       console.log("in Product ajax success");
        console.log(data);
        for (let i = 0; i < data.length; i++)
        {
         output += "<div class='card'><div class='row'><div class='col-sm-12'><img class='product-img' src={% static 'dist/img/image_77.png' %} alt='Card image' /><div class='card-body-right'><p class='sidebar-heading mb-0'>"+
                    data[i]["name"]  + " <span class='active-button'>Active</span></p>"+
                                "<p class='sidebar-description mb-0'><span class='card-text'>" + data[i]["description"] +"</span></p>"+
                                "<p class='sidebar-footer-text mb-0'>" + data[i]["selling_price"]+ "</p></div></div></div></div>";

        }
        $("#ps").html(output);
        for (let i = 0; i < data.length; i++)
        {
         pdsearch += "<div class='card'><div class='row'><div class='col-sm-12'><img class='product-img' src={% static 'dist/img/image_77.png' %} alt='Card image' /><div class='card-body-right'><p class='sidebar-heading mb-0'>"+
                    data[i]["name"]  + " <span class='active-button'>Active</span></p>"+
                                "<p class='sidebar-description mb-0'><span class='card-text'>" + data[i]["description"] +"</span></p>"+
                                "<p class='sidebar-footer-text mb-0'>" + data[i]["selling_price"]+ "</p></div></div></div></div>";

        }
        $("#productsearch").html(pdsearch);

    }
  })
});

</script>


//running
//output += "<tr><td>" + data[i]["quot_no"] + "</td><td>" + data[i]["name"] +
//                       "</td><td>" + data[i]["quot_status"] + "</td><td>" + data[i]["market_seg"] +
//                       "</td><td>" + data[i]["created_at"] + "</td><td>" + data[i]["created_by"] +
//                      "</td><td class='fw-bold'>R 320</td></tr>";
//        }



//output += "<tr><td><a href="+{% url 'quotation'+ data[]  %}" + data[i]["quot_no"] + "</td><td>" + data[i]["name"] +
//                       "</td><td>" + data[i]["quot_status"] + "</td><td>" + data[i]["market_seg"] +
//                       "</td><td>" + data[i]["created_at"] + "</td><td>" + data[i]["created_by"] +
//                      "</td><td class='fw-bold'>R 320</td></tr>";