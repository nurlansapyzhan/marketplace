import account_css from "./Account.module.css";
import MainBlock from "./MainInfo/MainBlock";
import AccountField from "./AccountField/AccountField";

function Account(props) {
    return (
        <div className={account_css.block}>
            <MainBlock/>
            <AccountField/>
        </div>
    );
}

export default Account;