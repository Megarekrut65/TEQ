<script setup>
import { ref } from "vue";
import ModalWindow from "@/components/ModalWindow.vue";
import { memberCreateApi, memberDeleteApi, memberListApi } from "@/js/api/member.js";
import { errorAlert } from "@/js/utility/utility.js";

const props = defineProps({
  testId:{
    required: true,
    type: String,
  }
});

const model = defineModel({default:false});

const members = ref([]);

memberListApi(props.testId).then((res) => {
  members.value.push(...res);
}).catch(errorAlert);

const email = ref("");

const addAllEmails = (emails) => {
  memberCreateApi(props.testId, {emails})
    .then(res=>{
      members.value.push(...(res.members));
      members.value.push(...(res.notFound.map(email=>({user:{email:email}}))));
    }).catch(errorAlert);
};

const addEmail = ()=>{
  addAllEmails([email.value])
  email.value = "";
};

const removeFromList = (member)=>{
  const index = members.value.indexOf(member);
  if (index > -1) {
    members.value.splice(index, 1);
  }
};

const removeMember = (member)=>{
  if(member.id){
    memberDeleteApi(member.id).then(() => removeFromList(member)).catch(errorAlert);
  }
  else {
    removeFromList(member);
  }
};

</script>

<template>
  <ModalWindow v-model="model">

  <div class="form">
    <form @submit.prevent="addEmail" action="#" class="mb-1">
      <div class="input-group">
        <span class="input-group-text">@</span>
        <input
          v-model.trim="email"
          type="email"
          maxlength="1000"
          class="form-control mb-0"
          :placeholder="$t('memberEmail')"
          required
        >
        <button class="btn btn-primary mb-0 mt-0" type="submit">{{$t('add')}}</button>
      </div>
    </form>

    <h3><i class="fa-solid fa-users"></i> {{$t('members')}}</h3>
    <div class="emails">
      <div class="email-item" v-for="member in members" :key="member">
        <div class="input-group">
          <span class="input-group-text"><i class="fa fa-xmark btn-hover text-danger" @click="()=>removeMember(member)"></i> </span>
          <p :class="`form-control mb-0 ${!member.id?'text-danger':''}`"><i class="fa-solid fa-user"></i> {{member.user.email}}</p>
        </div>
      </div>
    </div>
  </div>
  </ModalWindow>
</template>

<style scoped>

.form{
  height: 60vh;
  position: relative;
  display: flex;
  flex-direction: column;
}

.emails{
  width: 100%;
  border: 1px solid black;
  padding: 5px;
  overflow-y: auto;
  flex: 1;

}
</style>
