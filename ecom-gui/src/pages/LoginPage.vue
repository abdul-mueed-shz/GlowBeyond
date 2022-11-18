<template>
  <q-page padding class="row">
    <div class="col-12 col-md-9 flex flex-center">
      <div class="full-width" style="max-width: 700px">
        <q-form>
          <q-card class="q-pa-lg">
            <q-card-section>
              <div class="text-h4 text-weight-bold text-grey-9">LOG IN</div>
            </q-card-section>
            <q-card-section>
              <q-input type="text" label="Email">
                <template #prepend>
                  <q-icon name="mdi-mail"></q-icon>
                </template>
              </q-input>
              <q-input type="text" label="Password">
                <template #prepend>
                  <q-icon name="mdi-lock"></q-icon>
                </template>
              </q-input>
            </q-card-section>
            <q-card-actions class="flex flex-center">
              <q-btn class="bg-primary text-white" label="Sign In"></q-btn>
              <q-btn
                to="/"
                class="bg-primary text-white"
                label="Go Back"
              ></q-btn>
            </q-card-actions>
          </q-card>
        </q-form>
      </div>
    </div>

    <div class="col-md-3 gt-sm flex flex-center text-black">TEST</div>
  </q-page>
</template>

<script setup></script>
