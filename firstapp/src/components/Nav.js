/**
 * navigation bar
 */
import Btn from "./Btn";

function Nav() {
    return (
        
        <nav className="main-nav">
            <ul>
                <li><Btn name='Home'></Btn></li>
                <li><Btn name='Search'></Btn></li>
                <li><Btn name='Contact'></Btn></li>
            </ul>
        </nav>
        
    );
};

export default Nav;