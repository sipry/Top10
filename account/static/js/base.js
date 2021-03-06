function submit_form()
{
  document.create_list.submit();
}

window.onload = function(e){
    const themeSelect = document.getElementById('themes_selector');
    if(themeSelect)
        themeSelect.onchange = submit_form


    $('#save-boton').click(() => {
        if ($('#dropzone').find('div.row').length === 10){
            let item_list = []
            $.each($('#dropzone').find('div.row'), (i, ele) => {
                item_list.push(parseInt(ele.id, 10))
           })
            document.getElementById('item_list').value = item_list.toString();

            submit_form()


        }
        else {
            console.log('it has to be 10 items')
        }
    });


    $('.drag').draggable({
      appendTo: 'body',
      helper: 'clone'
    });

    $('#dropzone').droppable({
      activeClass: 'active',
      hoverClass: 'hover',
      accept: ":not(.ui-sortable-helper)", // Reject clones generated by sortable
      drop: function (e, ui) {
        var $el = $('<div class="drop-item">' + ui.draggable.html() + '</div>');
        var repeated = false;
        var max = 9
        if ($('#dropzone').find('div.row').length > max){
            return;
        }
        $.each($('#dropzone').find('div.row'), (i, ele) => {
            if (ele.id === $el.find('div.row')[0].id) {
                repeated = true;
            }
        })
        if(repeated) {
            return;
        }


        $el.append($('<button type="button" class="btn btn-default btn-xs remove"><span class="fas fa-minus-circle"></span></button>').click(function () { $(this).parent().detach(); }));
        $(this).append($el);
      }
    }).sortable({
      items: '.drop-item',
      sort: function() {
        // gets added unintentionally by droppable interacting with sortable
        // using connectWithSortable fixes this, but doesn't allow you to customize active/hoverClass options
        $( this ).removeClass( "active" );
      }
    });

}

