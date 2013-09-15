function refresh_needs() {
  $.get(
    window.location.pathname + '/needs',
    function(data) {
      $.each($('.need-progress'), function(i, item) {
        item = $(item);
        if (typeof(data) == "string") {
          data = JSON.parse(data);
        }
        var id = item.attr('data-id');
        if (!data[id]) return;
        bar = $(item.find('.bar')[0]);
        bar.width(data[id][0]*100/data[id][1] + '%');
        fa = $($('#fa-' + id)[0]);
        fa.html('' + data[id][0]);
      });
    });
}

window.setInterval(refresh_needs, 2500);