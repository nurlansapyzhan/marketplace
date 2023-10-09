import authorization_css from "./Authorization.module.css";


export function adjustAuthorizationBlockPosition() {
    const authorizationBlock = document.querySelector(`.${authorization_css.authorization_block}`);

    if (!authorizationBlock) {
        console.log('Элемент с классом .authorization_block не найден.');
        return;
    }

    const authorizationStyles = getComputedStyle(authorizationBlock);
    const authorizationWidth = authorizationStyles.getPropertyValue('width');
    const authorizationHeight = authorizationStyles.getPropertyValue('height');
    const authorizationPadding = authorizationStyles.getPropertyValue('padding');

    let leftFixed = '5px';
    let topFixed = '5px';

    if (parseFloat(window.innerWidth) > (parseFloat(authorizationWidth) + parseFloat(authorizationPadding) * 2 + 10)) {
        leftFixed = parseInt((window.innerWidth - parseFloat(authorizationWidth) - parseFloat(authorizationPadding) * 2) / 2) + 'px';
    }
    if (parseFloat(window.innerHeight) > (parseFloat(authorizationHeight) + parseFloat(authorizationPadding) * 2)) {
        topFixed = parseInt((window.innerHeight - parseFloat(authorizationHeight) - parseFloat(authorizationPadding) * 2) / 2) + 'px';
    }

    document.documentElement.style.setProperty('--left-fixed', leftFixed);
    document.documentElement.style.setProperty('--top-fixed', topFixed);

    function handleResize() {
        if (parseFloat(window.innerWidth) > (parseFloat(authorizationWidth) + parseFloat(authorizationPadding) * 2 + 10)) {
            leftFixed = parseInt((window.innerWidth - parseFloat(authorizationWidth) - parseFloat(authorizationPadding) * 2) / 2) + 'px';
        } else {
            leftFixed = '5px';
        }
        if (parseFloat(window.innerHeight) > (parseFloat(authorizationHeight) + parseFloat(authorizationPadding) * 2)) {
            topFixed = parseInt((window.innerHeight - parseFloat(authorizationHeight) - parseFloat(authorizationPadding) * 2) / 2) + 'px';
        } else {
            topFixed = '5px';
        }
        document.documentElement.style.setProperty('--left-fixed', leftFixed);
        document.documentElement.style.setProperty('--top-fixed', topFixed);
    }

    window.addEventListener('resize', handleResize);

    handleResize();
}