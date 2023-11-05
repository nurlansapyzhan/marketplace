import main_block_css from "./MainBlock.module.css";
import Avatar from "./Avatar/Avatar";
import MainBlockField from "./MainText/MainBlockField";

function MainBlock(props) {
    return (
        <div className={main_block_css.block}>
            <Avatar/>
            <MainBlockField/>
        </div>
    );
}

export default MainBlock;