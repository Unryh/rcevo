$('.extremum-click').click(function () { //нажимаем на extremum-click
	if ($(this).hasClass('open')) { //идет проверка: если у нажатого эелемнта есть класс open
		$(this).removeClass('open'); // то мы удаляем у него класс open
		$(this).siblings('.extremum-slide').hide(); //и скрываем соседние элементы с классом extremum-slide
	}
	else { // в противном случае (у элемента нет класса open)
		$(this).addClass('open'); // мы ему добавляем класс open
		$(this).siblings('.extremum-slide').show(); //а соседние элементы с классом extremum-slide показываем
	}
});
$('.less').click(function () {  //нажимаем на less
	if ($(this).hasClass('more_condition')) { //идет проверка: если у нажатого эелемнта есть класс more_condition
		$(this).removeClass('more_condition'); // то мы удаляем у него класс more_condition
		(this).innerHTML = 'меньше'; //заменяем текстовое содержимое в HTML на меньше
		$(this).parents('li').siblings('.hidden').show(); //а соседние элементы у его родителя li с классом hidden показываем
	}
	else { // в противном случае (у элемента нет класса more_condition)
		$(this).addClass('more_condition'); // мы ему добавляем класс more_condition
		(this).innerHTML = 'больше'; //заменяем текстовое содержимое в HTML на больше
		$(this).parents('li').siblings('.hidden').hide(); //а соседние элементы у его родителя li с классом hidden скрываем
	}
});