function Btn(props) {
    const clickHandler = () => console.log('clicked')
    return (
        <botton onClick={clickHandler}>
            {props.name}
        </botton>
    );
};

export default Btn;