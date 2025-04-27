<script setup>
defineProps({
    categories: {
        type: Array,
        required: true,
    },
    pasteMode: {
        type: Boolean,
        required: true,
    },
    addToPool: {
        type: Function,
        required: true,
    },
    copyFromPool: {
        type: Function,
        required: true,
    },
});
</script>

<template>
    <ul id="tree">
        <li v-for="category in categories" :key="category.id">
            <input type="checkbox" checked v-if="!pasteMode" />
            <span>{{ category.name }} <i class="fa fa-plus btn-hover"></i></span>
            <ul v-if="!pasteMode">
                <li v-for="item in category.items" :key="item">
                    <span>{{ item.text ? item.text : $t("empty") }}</span>
                </li>
            </ul>
        </li>
    </ul>
</template>

<style scoped>
ul {
    display: inline-block;
    0position: relative;
    float: left;
    clear: left;
    margin: 0.25em;
    padding: 0;
    background: pink;
}
ul:before {
    content: "";
    position: absolute;
    z-index: 1;
    top: 0.25em;
    right: auto;
    bottom: 0;
    left: 1.75em;
    margin: auto;
    border-right: dotted black 0.1em;
    width: 0;
    height: auto;
    0background: blue;
}
ul:after {
    content: "-";
    position: absolute;
    z-index: 3;
    top: 0;
    left: -0.5em;
    margin: 0.65em;
    padding: 0;
    width: 0.8em;
    height: 0.8em;
    text-align: center;
    line-height: 0.6em;
    font-size: 1em;
    background: blue;
}
ul > li {
    display: block;
    position: relative;
    float: left;
    clear: both;
    right: auto;
    padding-left: 1em;
    width: auto;
    text-align: center;
    color: white;
    background: gray;
}
ul > li > input {
    display: block;
    position: absolute;
    float: left;
    z-index: 4;
    margin: 0 0 0 -1em;
    padding: 0;
    width: 1em;
    height: 2em;
    font-size: 1em;
    opacity: 0;
    cursor: pointer;
}
ul > li > input:checked ~ ul:before {
    display: none;
}
ul > li > input:checked ~ ul:after {
    content: "+";
}
ul > li > input:checked ~ ul * {
    display: none;
}
ul > li > span {
    display: block;
    position: relative;
    float: left;
    z-index: 3;
    margin: 0.25em;
    padding: 0.25em;
    background: lightblue;
}
ul > li > span:after {
    content: "";
    display: block;
    position: absolute;
    left: -1em;
    top: 0;
    bottom: 0;
    margin: auto 0.25em auto 0.25em;
    border-top: dotted black 0.1em;
    width: 0.75em;
    height: 0;
}

ul > li:last-child:before {
    content: "";
    display: block;
    position: absolute;
    z-index: 2;
    top: 1em;
    left: 0;
    bottom: -0.25em;
    width: 0.75em;
    height: auto;
    background: lightblue;
}

#tree {
    position: relative;
    font-family: "Georgia";
}
#tree:before {
    left: 0.5em;
}
#tree:after {
    display: none;
}

/*decoration*/
ul,
ul > li:last-child:before {
    background: white;
}
ul > li {
    background: transparent;
}
ul:after {
    background: white;
    color: black;
    border: solid gray 1px;
    border-radius: 0.1em;
}
ul > li > span {
    border-radius: 0.25em;
    color: black;
    background: white;
}
ul > li > input ~ span:before {
    content: "";
    display: inline-block;
    margin: 0 0.25em 0 0;
    width: 1em;
    height: 1em;
    line-height: 1em;
    background: url("@/assets/images/collection-opened.png");
    background-repeat: no-repeat;
    background-size: contain;
}
ul > li > input:checked ~ span:before {
    background-image: url("@/assets/images/collection-closed.png");
}
</style>
