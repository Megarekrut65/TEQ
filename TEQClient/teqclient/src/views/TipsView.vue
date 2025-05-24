<script setup>
import SingleTip from "@/components/tips/SingleTip.vue";
import { FULL, MULTIPLE, SCRIPT, SCRIPT_UNITTEST, SHORT, SINGLE } from "@/js/types.js";
import MultipleTip from "@/components/tips/MultipleTip.vue";
import ShortTip from "@/components/tips/ShortTip.vue";
import FullTip from "@/components/tips/FullTip.vue";
import ScriptTip from "@/components/tips/ScriptTip.vue";
import UnittestTip from "@/components/tips/UnittestTip.vue";
import PythonListTip from "@/components/tips/PythonListTip.vue";
import CppListTip from "@/components/tips/CppListTip.vue";
import JavaListTip from "@/components/tips/JavaListTip.vue";

const sections = [
  { id: SINGLE, titleKey: 'singleTip.title' },
  { id: MULTIPLE, titleKey: 'multiTip.title' },
  { id: SHORT, titleKey: 'shortTip.title' },
  { id: FULL, titleKey: 'fullTip.title' },
  { id: SCRIPT, titleKey: 'scriptTip.title' },
  { id: SCRIPT_UNITTEST, titleKey: 'unittestTip.title' },
  { id: 'PYTHON_LIST', titleKey: 'pythonListTip.title' },
  { id: 'CPP_VECTOR', titleKey: 'cppListTip.title' },
  { id: 'JAVA_LIST', titleKey: 'javaListTip.title' },
];
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-12 mb-1">
        <h1 class="tip-title">{{$t('tips')}}</h1>
      </div>

      <div class="col-12">
        <ul class="mb-4">
          <li
            v-for="(section, index) in sections"
            :key="section.id"
          >
            <a :href="`#${section.id}`">{{ index + 1 }}. {{ $t(section.titleKey) }}</a>
          </li>
        </ul>
      </div>
    </div>


    <div class="row">
      <div :id="SINGLE" class="col-12 mb-4">
        <SingleTip :index="1"></SingleTip>
      </div>
      <div :id="MULTIPLE" class="col-12 mb-4">
        <MultipleTip :index="2"></MultipleTip>
      </div>
      <div :id="SHORT" class="col-12 mb-4">
        <ShortTip :index="3"></ShortTip>
      </div>
      <div :id="FULL" class="col-12 mb-4">
        <FullTip :index="4"></FullTip>
      </div>
      <div :id="SCRIPT" class="col-12 mb-4">
        <ScriptTip :index="5"></ScriptTip>
      </div>
      <div :id="SCRIPT_UNITTEST" class="col-12 mb-4">
        <UnittestTip :index="6"></UnittestTip>
      </div>
      <div id="PYTHON_LIST" class="col-12 mb-4">
        <PythonListTip :index="7"></PythonListTip>
      </div>
      <div id="CPP_VECTOR" class="col-12 mb-4">
        <CppListTip :index="8"></CppListTip>
      </div>
      <div id="JAVA_LIST" class="col-12 mb-4">
        <JavaListTip :index="9"></JavaListTip>
      </div>
    </div>
  </div>
</template>


<style scoped>

</style>
