<template>
  <!-- notice dialogRef here -->
  <q-dialog ref="dialogRef" @hide="onDialogHide">
    <q-card
      class="q-dialog-plugin full-width"
      style="max-width: 700px; height: 300px"
    >
      <q-card-section class="column full-height flex flex-center">
        <div class="row">
          <div>
            <q-icon
              size="52px"
              color="positive"
              name="mdi-emoticon-happy"
            ></q-icon>
          </div>
          <div class="text-h3 text-positive q-ml-sm">
            {{ text }}
          </div>
        </div>
        <div class="q-mt-xl q-gutter-x-md">
          <q-btn
            class="btn-measurements"
            color="primary"
            outline
            label="Close"
            @click="onCancelClick"
          />
          <q-btn
            class="btn-measurements"
            color="primary"
            label="Details"
            icon="mdi-cart"
            @click="onOKClick"
          />
        </div>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script>
import { useDialogPluginComponent } from "quasar";
import { APP_ROUTES } from "src/common/constants/_routes";
import { useRouter } from "vue-router";

export default {
  props: {
    text: {
      type: String,
      required: true,
    },
  },

  emits: [...useDialogPluginComponent.emits],

  setup() {
    // REQUIRED; must be called inside of setup()
    const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } =
      useDialogPluginComponent();
    // dialogRef      - Vue ref to be applied to QDialog
    // onDialogHide   - Function to be used as handler for @hide on QDialog
    // onDialogOK     - Function to call to settle dialog with "ok" outcome
    //                    example: onDialogOK() - no payload
    //                    example: onDialogOK({ /*.../* }) - with payload
    // onDialogCancel - Function to call to settle dialog with "cancel" outcome
    const router = useRouter();
    return {
      // This is REQUIRED;
      // Need to inject these (from useDialogPluginComponent() call)
      // into the vue scope for the vue html template
      dialogRef,
      onDialogHide,

      // other methods that we used in our vue html template;
      // these are part of our example (so not required)
      onOKClick() {
        // on OK, it is REQUIRED to
        // call onDialogOK (with optional payload)
        router.push({ name: APP_ROUTES.ACCOUNT_DETAILS.NAME });
        onDialogOK();
        // or with payload: onDialogOK({ ... })
        // ...and it will also hide the dialog automatically
      },

      // we can passthrough onDialogCancel directly
      onCancelClick: onDialogCancel,
    };
  },
};
</script>
