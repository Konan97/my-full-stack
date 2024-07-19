function Header(props) {
    const styles = {
        color: "black", fontSize: "40px"
    }
    return (
        <div>
            <h1 style={styles}> Hello, {props.firstName}!</h1>
        </div>
    );
};

export default Header;