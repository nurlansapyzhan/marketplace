import main_block_field_css from "./MainBlockField.module.css";

function MainBlockField(props) {
    return (
        <div className={main_block_field_css.field}>
            <p>Имя пользователя: John Due</p>
            <p>Наименование компании: ТОО Home Credit</p>
            <p>Номер телефона: 8(777) 315 67 89</p>
            <p>Категория товаров: Кросовки, Куртки, Калготки, Перчатки</p>
        </div>
    );
}

export default MainBlockField;